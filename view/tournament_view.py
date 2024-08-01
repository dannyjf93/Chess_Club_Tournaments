class TournamentView:
    def display_no_tournaments_message(self):
        print("There are no tournaments available.")

    def display_in_progress_tournaments(self, tournaments):
        print("\nIn-Progress Tournaments:")
        for index, tournament in enumerate(tournaments, start=1):
            print(f"{index}. {tournament.name} (Start Date: {tournament.start_date}, End Date: {tournament.end_date})")

    def display_completed_tournaments(self, tournaments):
        print("\nCompleted Tournaments:")
        for index, tournament in enumerate(tournaments, start=1):
            print(f"{index}. {tournament.name} (Start Date: {tournament.start_date}, End Date: {tournament.end_date})")

    def display_tournament_selection_prompt(self):
        print("Enter the number of the tournament to manage or 'b' to go back:")

    def display_tournament_details(self, tournament):
        print(f"\nTournament: {tournament.name}")
        print(f"Venue: {tournament.venue}")
        print(f"Start Date: {tournament.start_date}")
        print(f"End Date: {tournament.end_date}")

        if not tournament.is_completed():
            print(f"Current Round: {tournament.current_round} of {tournament.number_of_rounds}\n")
        else:
            print(f"Rounds Played: {tournament.number_of_rounds}\n")

        print("Finished Matches:")
        for round_number, matches in tournament.results.items():
            print(f"Round {round_number}:")
            for match in matches:
                if match.get('draw'):
                    print(f"Match: {match['player1']} (ID: {match['player1_id']}) vs {match['player2']} (ID: {match['player2_id']}) - Draw")
                else:
                    print(f"Match: {match['winner']} (ID: {match['winner_id']}) defeated {match['loser']} (ID: {match['loser_id']})")

        print("\nPlayers:")
        sorted_players = sorted(tournament.players, key=lambda player: tournament.scores[player['identifier']], reverse=True)
        for index, player in enumerate(sorted_players, start=1):
            club = player.get('club', 'No club')
            place = self.ordinal(index)
            print(f"{place} place: {player['name']} (ID: {player['identifier']}) - Club: {club}, Score: {tournament.scores[player['identifier']]}")

    def display_prompt_for_match_result(self, match, match_index):
        print(f"Match {match_index + 1}:")
        print(f"1. {match['player1']} (ID: {match['player1_id']}) wins")
        print(f"2. {match['player2']} (ID: {match['player2_id']}) wins")
        print(f"3. Draw")

    def display_invalid_choice_message(self):
        print("Invalid choice. Please try again.")

    @staticmethod
    def ordinal(n):
        return "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])
