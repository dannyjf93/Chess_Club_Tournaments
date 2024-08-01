import json
import os


class Player:
    def __init__(self, name, email, identifier, birthdate, club_name=None):
        self.name = name
        self.email = email
        self.identifier = identifier
        self.birthdate = birthdate
        self.club_name = club_name

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'identifier': self.identifier,
            'birthdate': self.birthdate,
            'club_name': self.club_name
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            email=data['email'],
            identifier=data['identifier'],
            birthdate=data['birthdate'],
            club_name=data.get('club_name')
        )

    @staticmethod
    def load_from_file(filename):
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            return [Player.from_dict(player_data) for player_data in json.load(f)]

    @staticmethod
    def save_to_file(players, filename):
        with open(filename, 'w') as f:
            json.dump([player.to_dict() for player in players], f, indent=4)
