import json
import os
import random
from model.tournament import Tournament
from model.club import Club
from model.player import Player


class TournamentController:
    def __init__(self):
        # Initialize the controller, load tournaments, clubs, and players from files
        self.filename = 'data/tournaments.json'
        self.tournaments = self.load_from_file()
        self.clubs = self.load_clubs()
        self.players = self.load_players()

    # Load tournaments from a JSON file
    def load_from_file(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            tournaments_data = json.load(f)
        tournaments = [Tournament.from_dict(data) for data in tournaments_data]
        return tournaments

    # Save tournaments to a JSON file
    def save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump([tournament.to_dict() for tournament in self.tournaments], f, indent=4)

    # Load clubs from a JSON file
    def load_clubs(self):
        filename = 'data/clubs.json'
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            clubs_data = json.load(f)
        clubs = [Club.from_dict(data) for data in clubs_data]
        return clubs

    # Load players from a JSON file
    def load_players(self):
        filename = 'data/players.json'
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            players_data = json.load(f)
        players = [Player.from_dict(data) for data in players_data]
        return players

    # Create a new tournament and save it to the file
    def create_tournament(self, name, venue, start_date, end_date, number_of_rounds):
        tournament = Tournament(name, venue, start_date, end_date, number_of_rounds)
        self.tournaments.append(tournament)
        self.save_to_file()

    # Register a player for a tournament
    def register_player(self, tournament_name, player):
        self.players = self.load_players()
        tournament = self.find_tournament(tournament_name)
        if tournament:
            for registered_player in tournament.players:
                if registered_player['identifier'] == player['identifier']:
                    print(f"Player {player['name']} is already registered for this tournament.")
                    return

            # Add the club name to the player dictionary
            player['club'] = self.get_player_club(player['identifier'])
            tournament.players.append(player)
            if player['identifier'] not in tournament.scores:
                tournament.scores[player['identifier']] = 0.0
            self.save_to_file()

    # Get the club name for a player based on their identifier
    def get_player_club(self, player_identifier):
        for club in self.clubs:
            for player in club.players:
                if player['identifier'] == player_identifier:
                    return club.name
        return "No club"

    # Enter match results for a specific round in a tournament
    def enter_results(self, tournament_name, round_number, match_results):
        tournament = self.find_tournament(tournament_name)
        if tournament:
            round_key = str(round_number)
            if round_key not in tournament.results:
                tournament.results[round_key] = []

            # Update existing matches or add new matches
            for result in match_results:
                match_found = False
                for match in tournament.results[round_key]:
                    if match['player1_id'] == result['player1_id'] and match['player2_id'] == result['player2_id']:
                        match['draw'] = result['draw']
                        if result['draw']:
                            # Remove winner and loser fields if draw is true
                            match.pop('winner', None)
                            match.pop('winner_id', None)
                            match.pop('loser', None)
                            match.pop('loser_id', None)
                        else:
                            match.update({
                                'winner': result['winner'],
                                'winner_id': result['winner_id'],
                                'loser': result['loser'],
                                'loser_id': result['loser_id']
                            })
                        match_found = True
                        break
                if not match_found:
                    match_entry = {
                        'player1': result['player1'],
                        'player1_id': result['player1_id'],
                        'player2': result['player2'],
                        'player2_id': result['player2_id'],
                        'draw': result['draw']
                    }
                    if not result['draw']:
                        match_entry.update({
                            'winner': result['winner'],
                            'winner_id': result['winner_id'],
                            'loser': result['loser'],
                            'loser_id': result['loser_id']
                        })
                    tournament.results[round_key].append(match_entry)

            self.update_scores(tournament, match_results)
            self.save_to_file()
            return True  # Indicate that results were successfully entered

    # Edit match results for a specific round in a tournament
    def edit_results(self, tournament_name, round_number, match_index, new_result):
        tournament = self.find_tournament(tournament_name)
        if tournament:
            old_result = tournament.results[str(round_number)][match_index]
            self.revert_scores(tournament, old_result)
            match = tournament.results[str(round_number)][match_index]
            match['draw'] = new_result['draw']
            if new_result['draw']:
                # Remove winner and loser fields if draw is true
                match.pop('winner', None)
                match.pop('winner_id', None)
                match.pop('loser', None)
                match.pop('loser_id', None)
                match.update({
                    'player1': new_result['player1'],
                    'player1_id': new_result['player1_id'],
                    'player2': new_result['player2'],
                    'player2_id': new_result['player2_id']
                })
            else:
                match.update({
                    'winner': new_result['winner'],
                    'winner_id': new_result['winner_id'],
                    'loser': new_result['loser'],
                    'loser_id': new_result['loser_id']
                })
            self.update_scores(tournament, [new_result])
            self.save_to_file()

    # Update scores for players based on match results
    def update_scores(self, tournament, results):
        for result in results:
            if result.get('draw'):
                tournament.scores[result['player1_id']] += 0.5
                tournament.scores[result['player2_id']] += 0.5
            else:
                tournament.scores[result['winner_id']] += 1.0

    # Revert scores for players based on old match results
    def revert_scores(self, tournament, result):
        if result.get('draw'):
            tournament.scores[result['player1_id']] -= 0.5
            tournament.scores[result['player2_id']] -= 0.5
        elif 'winner_id' in result:
            tournament.scores[result['winner_id']] -= 1.0

    # Advance to the next round in a tournament
    def advance_round(self, tournament_name):
        tournament = self.find_tournament(tournament_name)
        if tournament:
            tournament.current_round += 1
            self.save_to_file()

    # Find a tournament by name
    def find_tournament(self, name):
        for tournament in self.tournaments:
            if tournament.name == name:
                return tournament
        return None

    # Pair players for matches in the current round
    def pair_players(self, tournament):
        if tournament.current_round == 1:
            # Random pairing for the first round
            players = tournament.players[:]
            random.shuffle(players)
            matches = [(players[i], players[i + 1]) for i in range(0, len(players), 2)]
        else:
            # Pair players based on scores for subsequent rounds
            players = sorted(tournament.players, key=lambda p: tournament.scores[p['identifier']], reverse=True)
            matches = [(players[i], players[i + 1]) for i in range(0, len(players), 2)]

        round_key = str(tournament.current_round)
        tournament.results[round_key] = [
            {'player1': match[0]['name'], 'player1_id': match[0]['identifier'], 'player2': match[1]['name'],
             'player2_id': match[1]['identifier'], 'draw': None} for match in matches]
        self.save_to_file()
        return tournament.results[round_key]

    # Get a list of in-progress tournaments
    def report_in_progress(self):
        return [tournament for tournament in self.tournaments if not tournament.is_completed()]

    # Get a list of completed tournaments
    def report_completed(self):
        completed_tournaments = [tournament for tournament in self.tournaments if tournament.is_completed()]
        completed_tournaments.sort(key=lambda x: x.end_date, reverse=True)
        return completed_tournaments

    # Mark a tournament as completed
    def mark_tournament_completed(self, tournament_name):
        tournament = self.find_tournament(tournament_name)
        if tournament:
            if not self.all_rounds_completed(tournament):
                print("Cannot mark the tournament as completed. Not all round results are recorded.")
                return
            tournament.completed = True
            self.save_to_file()
            print("Tournament marked as completed.")

    # Confirm all round results have been recorded
    def all_rounds_completed(self, tournament):
        for round_number in range(1, tournament.number_of_rounds + 1):
            if str(round_number) not in tournament.results or not tournament.results[str(round_number)]:
                return False
        return True

    # Save tournaments to a JSON file (duplicate of save_to_file, included for completeness)
    def save_tournaments(self):
        with open(self.filename, 'w') as f:
            json.dump([tournament.to_dict() for tournament in self.tournaments], f, indent=4)
