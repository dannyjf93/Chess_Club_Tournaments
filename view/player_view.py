class PlayerView:
    # Display a list of players along with their club names
    def display_players_with_clubs(self, players, tournament_controller):
        for index, player in enumerate(players, start=1):
            # Get the club name for each player using the tournament controller
            club_name = tournament_controller.get_player_club(player.identifier)
            print(f"{index}. {player.name} (ID: {player.identifier}) - Club: {club_name}")

    # Display search results for players along with their club names
    def display_search_results(self, players, tournament_controller):
        if not players:
            # If no players found, display a message
            print("No players found.")
        else:
            # If players are found, display them with their club names
            for index, player in enumerate(players, start=1):
                # Get the club name for each player using the tournament controller
                club_name = tournament_controller.get_player_club(player.identifier)
                print(f"{index}. {player.name} (ID: {player.identifier}) - Club: {club_name}")

    # Display prompt for player selection
    def display_player_selection_prompt(self):
        print("\nEnter the number of the player to select or 'b' to go back:")
