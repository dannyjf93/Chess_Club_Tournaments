import json

class Club:
    def __init__(self, name, players=None):
        # Initialize club attributes
        self.name = name
        self.players = players if players is not None else []

    # Convert club object to dictionary
    def to_dict(self):
        return {
            'name': self.name,
            'players': self.players
        }

    # Create a club object from a dictionary
    @staticmethod
    def from_dict(data):
        return Club(data['name'], data['players'])

    # Load clubs from a JSON file
    @staticmethod
    def load_from_file(filename):
        # Open the file and load the data, creating Club objects from the dictionary data
        with open(filename, 'r') as f:
            data = json.load(f)
            return [Club.from_dict(club) for club in data]

    # Save clubs to a JSON file
    @staticmethod
    def save_to_file(clubs, filename):
        # Convert each club object to a dictionary and write to the file
        with open(filename, 'w') as f:
            json.dump([club.to_dict() for club in clubs], f, indent=4)
