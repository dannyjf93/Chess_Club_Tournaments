import json
import os
from model.club import Club
from model.player import Player

class ClubController:
    def __init__(self):
        self.filename = 'data/clubs.json'
        self.players_filename = 'data/players.json'
        self.clubs = self.load_from_file()
        self.players = self.load_players()

    def load_from_file(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as f:
            clubs_data = json.load(f)
        clubs = [Club.from_dict(data) for data in clubs_data]
        return clubs

    def save_to_file(self):
        with open(self.filename, 'w') as f:
            json.dump([club.to_dict() for club in self.clubs], f, indent=4)

    def load_players(self):
        if not os.path.exists(self.players_filename):
            return []
        with open(self.players_filename, 'r') as f:
            players_data = json.load(f)
        players = [Player.from_dict(data) for data in players_data]
        return players

    def save_players(self):
        with open(self.players_filename, 'w') as f:
            json.dump([player.to_dict() for player in self.players], f, indent=4)

    def create_club(self, name):
        club = Club(name)
        self.clubs.append(club)
        self.save_to_file()

    def view_clubs(self):
        return self.clubs

    def view_players_by_club(self, club_name):
        for club in self.clubs:
            if club.name == club_name:
                return club.players
        return []

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
