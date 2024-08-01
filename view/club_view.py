class ClubView:
    def display_clubs(self, clubs):
        if not clubs:
            print("No clubs available.")
        else:
            for index, club in enumerate(clubs):
                print(f"{index + 1}. Club: {club.name}, Players: {len(club.players)}")

    def display_no_clubs_message(self):
        print("No clubs available.")

    def display_players(self, players):
        if not players:
            print("There are no players registered for this club.")
        else:
            for index, player in enumerate(players):
                print(f"{index + 1}. Player: {player['name']}, Chess ID: {player['identifier']}")

    def display_no_players_message(self):
        print("There are no players registered for this club.")

    def display_club_selection_prompt(self):
        print("\nSelect a club by number or type 'B' to go back:")

    def display_player_selection_prompt(self):
        print("\nSelect a player by number to edit or type 'B' to go back:")

    def display_edit_player_prompt(self):
        print("Enter new values for the player's attributes (leave blank to keep current value):")
