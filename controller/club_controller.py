import json
import os
from model.club import Club
from model.player import Player

class ClubController:
    def __init__(self):
        # Initialize the controller, load clubs and players from files
        self.filename = 'data/clubs.json'
        self.players_filename = 'data/players.json'
        self.clubs = self.load_from_file()
        self.players = self.load_players()

    # Load clubs from a JSON file
    def load_from_file(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            clubs_data = json.load(f)
        clubs = [Club.from_dict(data) for data in clubs_data]
        return clubs

    # Save clubs to a JSON file
    def save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump([club.to_dict() for club in self.clubs], f, indent=4)

    # Load players from a JSON file
    def load_players(self):
        if not os.path.exists(self.players_filename):
            return []
        with open(self.players_filename, 'r') as f:
            players_data = json.load(f)
        players = [Player.from_dict(data) for data in players_data]
        return players

    # Save players to a JSON file
    def save_players(self):
        with open(self.players_filename, 'w') as f:
            json.dump([player.to_dict() for player in self.players], f, indent=4)

    # Create a new club and save it to the file
    def create_club(self, name):
        club = Club(name)
        self.clubs.append(club)
        self.save_to_file()

    # Return the list of clubs
    def view_clubs(self):
        return self.clubs

    # Return the list of players for a specific club
    def view_players_by_club(self, club_name):
        for club in self.clubs:
            if club.name == club_name:
                return club.players
        return []

    # Add a player to a club and save the updated club and player data to the files
    def add_player_to_club(self, club_name, player_data):
        player = Player.from_dict(player_data)
        player.club_name = club_name  # Set the club_name for the player
        for club in self.clubs:
            if club.name == club_name:
                club.players.append(player.to_dict())
                self.players.append(player)
                self.save_to_file()
                self.save_players()
                break
