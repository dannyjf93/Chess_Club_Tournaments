import json
import os


class Player:
    def __init__(self, name, email, identifier, birthdate, club_name=None):
        # Initialize player attributes
        self.name = name
        self.email = email
        self.identifier = identifier
        self.birthdate = birthdate
        self.club_name = club_name

    # Convert player object to dictionary
    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'identifier': self.identifier,
            'birthdate': self.birthdate,
            'club_name': self.club_name
        }

    # Create a player object from a dictionary
    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            email=data['email'],
            identifier=data['identifier'],
            birthdate=data['birthdate'],
            club_name=data.get('club_name')
        )

    # Load players from a JSON file
    @staticmethod
    def load_from_file(filename):
        # If the file doesn't exist, return an empty list
        if not os.path.exists(filename):
            return []
        # Open the file and load the data, creating Player objects from the dictionary data
        with open(filename, 'r') as f:
            return [Player.from_dict(player_data) for player_data in json.load(f)]

    # Save players to a JSON file
    @staticmethod
    def save_to_file(players, filename):
        # Convert each player object to a dictionary and write to the file
        with open(filename, 'w') as f:
            json.dump([player.to_dict() for player in players], f, indent=4)
