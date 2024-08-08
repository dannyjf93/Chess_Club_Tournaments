from model.player import Player


class PlayerController:
    def __init__(self, filename='data/players.json'):
        # Initialize the controller with the filename for storing player data
        self.filename = filename
        # Load players from the specified file
        self.players = Player.load_from_file(self.filename)

    # Add a new player and save the updated player list to the file
    def add_player(self, name, email, identifier, birthdate):
        # Create a new player object
        new_player = Player(name, email, identifier, birthdate)
        # Add the new player to the list of players
        self.players.append(new_player)
        # Save the updated list of players to the file
        Player.save_to_file(self.players, self.filename)

    # Return the list of players
    def view_players(self):
        return self.players

    def refresh_players(self):
        self.players = Player.load_from_file(self.filename)
