class ClubView:
    # Display a list of clubs with the number of players in each club
    def display_clubs(self, clubs):
        if not clubs:
            # If there are no clubs, display a message
            print("No clubs available.")
        else:
            # If there are clubs, list them with the number of players in each club
            for index, club in enumerate(clubs):
                print(f"{index + 1}. Club: {club.name}, Players: {len(club.players)}")

    # Display message when there are no clubs available
    def display_no_clubs_message(self):
        print("No clubs available.")

    # Display a list of players in a club
    def display_players(self, players):
        if not players:
            # If there are no players in the club, display a message
            print("There are no players registered for this club.")
        else:
            # If there are players, list them with their names and chess IDs
            for index, player in enumerate(players):
                print(f"{index + 1}. Player: {player['name']}, Chess ID: {player['identifier']}")

    # Display message when there are no players registered in a club
    def display_no_players_message(self):
        print("There are no players registered for this club.")

    # Display prompt for selecting a club
    def display_club_selection_prompt(self):
        print("\nSelect a club by number or type 'B' to go back:")

    # Display prompt for selecting a player to edit
    def display_player_selection_prompt(self):
        print("\nSelect a player by number to edit or type 'B' to go back:")

    # Display prompt for editing player attributes
    def display_edit_player_prompt(self):
        print("Enter new values for the player's attributes (leave blank to keep current value):")
