import json


class Club:
    def __init__(self, name, players=None):
        self.name = name
        self.players = players if players is not None else []

    def to_dict(self):
        return {
            'name': self.name,
            'players': self.players
        }

    @staticmethod
    def from_dict(data):
        return Club(data['name'], data['players'])

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            return [Club.from_dict(club) for club in data]

    @staticmethod
    def save_to_file(clubs, filename):
        with open(filename, 'w') as f:
            json.dump([club.to_dict() for club in clubs], f, indent=4)
