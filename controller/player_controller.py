from model.player import Player


class PlayerController:
    def __init__(self, filename='data/players.json'):
        self.filename = filename
        self.players = Player.load_from_file(self.filename)

    def add_player(self, name, email, identifier, birthdate):
        new_player = Player(name, email, identifier, birthdate)
        self.players.append(new_player)
        Player.save_to_file(self.players, self.filename)

    def view_players(self):
        return self.players
