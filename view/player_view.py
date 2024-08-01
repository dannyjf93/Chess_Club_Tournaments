class PlayerView:
    def display_players_with_clubs(self, players, tournament_controller):
        for index, player in enumerate(players, start=1):
            club_name = tournament_controller.get_player_club(player.identifier)
            print(f"{index}. {player.name} (ID: {player.identifier}) - Club: {club_name}")

    def display_search_results(self, players, tournament_controller):
        if not players:
            print("No players found.")
        else:
            for index, player in enumerate(players, start=1):
                club_name = tournament_controller.get_player_club(player.identifier)
                print(f"{index}. {player.name} (ID: {player.identifier}) - Club: {club_name}")

    def display_player_selection_prompt(self):
        print("\nEnter the number of the player to select or 'b' to go back:")
