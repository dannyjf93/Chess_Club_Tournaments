import os
import json
from controller.club_controller import ClubController
from controller.player_controller import PlayerController
from controller.tournament_controller import TournamentController
from model.club import Club
from model.player import Player
from view.club_view import ClubView
from view.player_view import PlayerView
from view.tournament_view import TournamentView


# Function to initialize data files if they don't exist
def initialize_data_files():
    data_files = {
        'data/clubs.json': [],
        'data/players.json': [],
        'data/tournaments.json': []
    }

    # Create the 'data' directory if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')

    # Create the data files with default content if they don't exist
    for file, default_content in data_files.items():
        if not os.path.exists(file):
            with open(file, 'w') as f:
                json.dump(default_content, f, indent=4)


# Main function
def main():
    initialize_data_files()

    # Initialize controllers and views
    club_controller = ClubController()
    player_controller = PlayerController()
    tournament_controller = TournamentController()
    club_view = ClubView()
    player_view = PlayerView()
    tournament_view = TournamentView()

    # Main menu loop
    while True:
        print("\n1. Manage Clubs\n2. Create New Tournament\n3. View/Manage Tournament\n4. Reports\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            # Manage Clubs menu loop
            while True:
                print("\n1. View Existing Clubs\n2. Create New Club\n3. View Players by Club\n4. Add New Player to "
                      "Club\n5. Back")
                sub_choice = input("Enter your choice: ")

                if sub_choice == '1':
                    # View existing clubs
                    clubs = club_controller.view_clubs()
                    if not clubs:
                        club_view.display_no_clubs_message()
                    else:
                        club_view.display_clubs(clubs)
                elif sub_choice == '2':
                    # Create a new club
                    name = input("Enter club name: ")
                    club_controller.create_club(name)
                elif sub_choice == '3':
                    # View players by club
                    clubs = club_controller.view_clubs()
                    if not clubs:
                        club_view.display_no_clubs_message()
                    else:
                        club_view.display_clubs(clubs)
                        club_view.display_club_selection_prompt()
                        club_choice = input("Enter your choice: ")
                        if club_choice.lower() == 'b':
                            continue
                        try:
                            club_index = int(club_choice) - 1
                            if 0 <= club_index < len(clubs):
                                players = club_controller.view_players_by_club(clubs[club_index].name)
                                if not players:
                                    club_view.display_no_players_message()
                                else:
                                    club_view.display_players(players)
                                    club_view.display_player_selection_prompt()
                                    player_choice = input("Enter your choice: ")
                                    if player_choice.lower() == 'b':
                                        continue
                                    try:
                                        player_index = int(player_choice) - 1
                                        if 0 <= player_index < len(players):
                                            player = players[player_index]
                                            club_view.display_edit_player_prompt()
                                            new_name = input(f"Name [{player['name']}]: ").strip()
                                            new_email = input(f"Email [{player['email']}]: ").strip()
                                            new_identifier = input(f"Identifier [{player['identifier']}]: ").strip()
                                            new_birthdate = input(f"Birthdate [{player['birthdate']}]: ").strip()

                                            # Update player details if new values are provided
                                            player['name'] = new_name if new_name else player['name']
                                            player['email'] = new_email if new_email else player['email']
                                            player['identifier'] = new_identifier \
                                                if new_identifier else player['identifier']
                                            player['birthdate'] = new_birthdate \
                                                if new_birthdate else player['birthdate']

                                            # Save updated details
                                            Club.save_to_file(club_controller.clubs, club_controller.filename)
                                            Player.save_to_file(player_controller.players, player_controller.filename)
                                            print("Player details updated successfully.")
                                        else:
                                            print("Invalid selection. Please try again.")
                                    except ValueError:
                                        print("Invalid input. Please enter a number.")
                            else:
                                print("Invalid selection. Please try again.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                elif sub_choice == '4':
                    # Add new player to a club
                    clubs = club_controller.view_clubs()
                    if not clubs:
                        club_view.display_no_clubs_message()
                    else:
                        club_view.display_clubs(clubs)
                        club_view.display_club_selection_prompt()
                        club_choice = input("Enter your choice: ")
                        if club_choice.lower() == 'b':
                            continue
                        try:
                            club_index = int(club_choice) - 1
                            if 0 <= club_index < len(clubs):
                                club_name = clubs[club_index].name
                                player_name = input("Enter player name: ")
                                email = input("Enter email: ")
                                identifier = input("Enter identifier: ")
                                birthdate = input("Enter birthdate: ")
                                player_data = {
                                    'name': player_name,
                                    'email': email,
                                    'identifier': identifier,
                                    'birthdate': birthdate
                                }
                                club_controller.add_player_to_club(club_name, player_data)
                            else:
                                print("Invalid selection. Please try again.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                elif sub_choice == '5':
                    # Go back to the main menu
                    break

        elif choice == '2':
            # Create a new tournament
            name = input("Enter tournament name: ")
            venue = input("Enter venue: ")
            start_date = input("Enter start date: ")
            end_date = input("Enter end date: ")
            rounds = int(input("Enter number of rounds: "))
            tournament_controller.create_tournament(name, venue, start_date, end_date, rounds)

        elif choice == '3':
            # View/Manage tournament menu loop
            while True:
                tournaments = tournament_controller.report_in_progress()
                if not tournaments:
                    tournament_view.display_no_tournaments_message()
                    break
                tournament_view.display_in_progress_tournaments(tournaments)
                tournament_view.display_tournament_selection_prompt()
                tournament_choice = input("Enter your choice: ")
                if tournament_choice.lower() == 'b':
                    break
                try:
                    tournament_index = int(tournament_choice) - 1
                    if 0 <= tournament_index < len(tournaments):
                        selected_tournament = tournaments[tournament_index]
                        while True:
                            current_round_info = (f"Current Round: {selected_tournament.current_round}"
                                                  f" of {selected_tournament.number_of_rounds}")
                            print(f"\nManaging Tournament: {selected_tournament.name}. {current_round_info}")
                            print("1. Register player for tournament\n2. Enter results for current round"
                                  "\n3. Advance to the next round\n4. Mark tournament as completed"
                                  "\n5. View registered players\n6. Back")
                            sub_choice = input("Enter your choice: ")

                            if sub_choice == '1':
                                # Check if any results have been recorded
                                if any(selected_tournament.results.values()):
                                    print("Cannot register new players as results have already been recorded for this "
                                          "tournament.")
                                else:
                                    print("\n1. Select from list of all players\n2. Search for player by chess "
                                          "identifier\n3. Search for player by name (case insensitive)\n4. Back")
                                    register_choice = input("Enter your choice: ")

                                    if register_choice == '1':
                                        # Select from list of all players
                                        players = player_controller.view_players()
                                        player_view.display_players_with_clubs(players, tournament_controller)
                                        player_view.display_player_selection_prompt()
                                        player_choice = input("Enter your choice: ")
                                        if player_choice.lower() == 'b':
                                            continue
                                        try:
                                            player_index = int(player_choice) - 1
                                            if 0 <= player_index < len(players):
                                                player = players[player_index].to_dict()
                                                tournament_controller.register_player(selected_tournament.name, player)
                                            else:
                                                print("Invalid selection. Please try again.")
                                        except ValueError:
                                            print("Invalid input. Please enter a number.")

                                    elif register_choice == '2':
                                        # Search for player by chess identifier
                                        identifier = input("Enter chess identifier: ")
                                        players = [p for p in player_controller.view_players()
                                                   if p.identifier == identifier]
                                        player_view.display_search_results(players, tournament_controller)
                                        if players:
                                            player_view.display_player_selection_prompt()
                                            player_choice = input("Enter your choice: ")
                                            if player_choice.lower() == 'b':
                                                continue
                                            try:
                                                player_index = int(player_choice) - 1
                                                if 0 <= player_index < len(players):
                                                    player = players[player_index].to_dict()
                                                    tournament_controller.register_player(
                                                        selected_tournament.name, player)
                                                else:
                                                    print("Invalid selection. Please try again.")
                                            except ValueError:
                                                print("Invalid input. Please enter a number.")

                                    elif register_choice == '3':
                                        # Search for player by name
                                        name_part = input("Enter part of player's name: ").lower()
                                        players = [p for p in player_controller.view_players()
                                                   if name_part in p.name.lower()]
                                        player_view.display_search_results(players, tournament_controller)
                                        if players:
                                            player_view.display_player_selection_prompt()
                                            player_choice = input("Enter your choice: ")
                                            if player_choice.lower() == 'b':
                                                continue
                                            try:
                                                player_index = int(player_choice) - 1
                                                if 0 <= player_index < len(players):
                                                    player = players[player_index].to_dict()
                                                    tournament_controller.register_player(
                                                        selected_tournament.name, player)
                                                else:
                                                    print("Invalid selection. Please try again.")
                                            except ValueError:
                                                print("Invalid input. Please enter a number.")
                                    elif register_choice == '4':
                                        continue

                            elif sub_choice == '2':
                                # Enter results for the current round
                                if len(selected_tournament.players) < 2:
                                    print("There are not enough players registered to begin this tournament.")
                                elif len(selected_tournament.players) % 2 != 0:
                                    print("The number of registered players must be even to begin this tournament.")
                                else:
                                    round_number = selected_tournament.current_round

                                    if (str(round_number) in selected_tournament.results
                                            and selected_tournament.results[str(round_number)]):
                                        print("Results for this round already exist.")
                                        edit_choice = input("Edit results for current round? (y/n): ").lower()
                                        if edit_choice == 'y':
                                            matches = selected_tournament.results[str(round_number)]
                                            while True:
                                                for index, match in enumerate(matches):
                                                    print(f"Match {index + 1}:")
                                                    player1_name = match['player1']
                                                    player2_name = match['player2']
                                                    print(f"1. {player1_name} wins")
                                                    print(f"2. {player2_name} wins")
                                                    print("3. Draw")
                                                match_index = int(input("Select a match to edit by number: ")) - 1
                                                if 0 <= match_index < len(matches):
                                                    match = matches[match_index]
                                                    player1_name = match['player1']
                                                    player2_name = match['player2']
                                                    new_result_choice = input("Enter your choice: ")
                                                    if new_result_choice == '1':
                                                        new_result = {
                                                            'player1': player1_name,
                                                            'player1_id': match['player1_id'],
                                                            'player2': player2_name,
                                                            'player2_id': match['player2_id'],
                                                            'winner': player1_name,
                                                            'winner_id': match['player1_id'],
                                                            'loser': player2_name,
                                                            'loser_id': match['player2_id'],
                                                            'draw': False
                                                        }
                                                    elif new_result_choice == '2':
                                                        new_result = {
                                                            'player1': player1_name,
                                                            'player1_id': match['player1_id'],
                                                            'player2': player2_name,
                                                            'player2_id': match['player2_id'],
                                                            'winner': player2_name,
                                                            'winner_id': match['player2_id'],
                                                            'loser': player1_name,
                                                            'loser_id': match['player1_id'],
                                                            'draw': False
                                                        }
                                                    elif new_result_choice == '3':
                                                        new_result = {
                                                            'player1': player1_name,
                                                            'player1_id': match['player1_id'],
                                                            'player2': player2_name,
                                                            'player2_id': match['player2_id'],
                                                            'draw': True
                                                        }
                                                    else:
                                                        print("Invalid choice. Please try again.")
                                                        continue

                                                    tournament_controller.edit_results(
                                                        selected_tournament.name,
                                                        round_number, match_index, new_result)
                                                    break
                                            break
                                    else:
                                        matches = tournament_controller.pair_players(selected_tournament)
                                        for match_index, match in enumerate(matches):
                                            while True:
                                                player1 = match['player1']
                                                player2 = match['player2']
                                                print(f"Match {match_index + 1}: {player1} vs {player2}")
                                                print(f"1. {player1} wins")
                                                print(f"2. {player2} wins")
                                                print("3. Draw")
                                                result_choice = input("Enter your choice: ")
                                                if result_choice == '1':
                                                    match_results = {
                                                        'player1': player1,
                                                        'player1_id': match['player1_id'],
                                                        'player2': player2,
                                                        'player2_id': match['player2_id'],
                                                        'winner': player1,
                                                        'winner_id': match['player1_id'],
                                                        'loser': player2,
                                                        'loser_id': match['player2_id'],
                                                        'draw': False
                                                    }
                                                elif result_choice == '2':
                                                    match_results = {
                                                        'player1': player1,
                                                        'player1_id': match['player1_id'],
                                                        'player2': player2,
                                                        'player2_id': match['player2_id'],
                                                        'winner': player2,
                                                        'winner_id': match['player2_id'],
                                                        'loser': player1,
                                                        'loser_id': match['player1_id'],
                                                        'draw': False
                                                    }
                                                elif result_choice == '3':
                                                    match_results = {
                                                        'player1': player1,
                                                        'player1_id': match['player1_id'],
                                                        'player2': player2,
                                                        'player2_id': match['player2_id'],
                                                        'draw': True
                                                    }
                                                else:
                                                    print("Invalid choice. Please try again.")
                                                    continue

                                                tournament_controller.enter_results(
                                                    selected_tournament.name, round_number, [match_results])
                                                break

                            elif sub_choice == '3':
                                # Advance to the next round
                                if len(selected_tournament.players) < 2:
                                    print("There are not enough players registered to begin this tournament.")
                                elif len(selected_tournament.players) % 2 != 0:
                                    print("The number of registered players must be even to begin this tournament.")
                                else:
                                    if selected_tournament.current_round == selected_tournament.number_of_rounds:
                                        if (str(selected_tournament.current_round)
                                                not in selected_tournament.results
                                                or not selected_tournament.results[str(
                                                    selected_tournament.current_round)]):
                                            print("Cannot continue without recording the results for the final round.")
                                        else:
                                            print("All rounds have already been played.")
                                    else:
                                        if (str(selected_tournament.current_round)
                                                in selected_tournament.results
                                                and selected_tournament.results[str(
                                                    selected_tournament.current_round)]):
                                            confirm_choice = input("Are you sure you want to advance to the next "
                                                                   "round? [y/n]: ").lower()
                                            if confirm_choice == 'y':
                                                tournament_controller.advance_round(selected_tournament.name)
                                                print("Advanced to the next round.")
                                            else:
                                                print("Stayed on the current round.")
                                        else:
                                            print("You must enter the results for the current round before advancing "
                                                  "to the next round.")

                            elif sub_choice == '4':
                                # Mark tournament as completed
                                if len(selected_tournament.players) < 2:
                                    print("There are not enough players registered to begin this tournament.")
                                elif len(selected_tournament.players) % 2 != 0:
                                    print("The number of registered players must be even to begin this tournament.")
                                else:
                                    if len(selected_tournament.results) < selected_tournament.number_of_rounds:
                                        print("Cannot mark the tournament as completed. Not all round results are "
                                              "recorded.")
                                    else:
                                        complete_choice = input("Mark tournament as completed? (y/n): ").lower()
                                        if complete_choice == 'y':
                                            tournament_controller.mark_tournament_completed(selected_tournament.name)
                                            print("You can now view the completed tournament in the Reports menu.")
                                            break

                            elif sub_choice == '5':
                                # View registered players
                                if not selected_tournament.players:
                                    print("No players have been registered for this tournament yet.")
                                else:
                                    print("\nRegistered Players:")
                                    for index, player in enumerate(selected_tournament.players, start=1):
                                        club_name = tournament_controller.get_player_club(player['identifier'])
                                        print(f"{index}. {player['name']}"
                                              f" (ID: {player['identifier']}) - Club: {club_name}")
                            elif sub_choice == '6':
                                # Go back to the previous menu
                                break
                            else:
                                print("Invalid selection. Please try again.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice == '4':
            # Reports menu loop
            while True:
                print("\n1. Tournaments in progress\n2. Completed tournaments\n3. Back")
                sub_choice = input("Enter your choice: ")

                if sub_choice == '1':
                    # Display tournaments in progress
                    tournaments = tournament_controller.report_in_progress()
                    if not tournaments:
                        tournament_view.display_no_tournaments_message()
                        continue
                    while True:
                        tournament_view.display_in_progress_tournaments(tournaments)
                        tournament_view.display_tournament_selection_prompt()
                        tournament_choice = input("Enter your choice: ")
                        if tournament_choice.lower() == 'b':
                            break
                        try:
                            tournament_index = int(tournament_choice) - 1
                            if 0 <= tournament_index < len(tournaments):
                                selected_tournament = tournaments[tournament_index]
                                tournament_view.display_tournament_details(selected_tournament)
                                break
                            else:
                                print("Invalid selection. Please try again.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                elif sub_choice == '2':
                    # Display completed tournaments
                    tournaments = tournament_controller.report_completed()
                    if not tournaments:
                        tournament_view.display_no_tournaments_message()
                        continue
                    while True:
                        tournament_view.display_completed_tournaments(tournaments)
                        tournament_view.display_tournament_selection_prompt()
                        tournament_choice = input("Enter your choice: ")
                        if tournament_choice.lower() == 'b':
                            break
                        try:
                            tournament_index = int(tournament_choice) - 1
                            if 0 <= tournament_index < len(tournaments):
                                selected_tournament = tournaments[tournament_index]
                                tournament_view.display_tournament_details(selected_tournament)
                                break
                            else:
                                print("Invalid selection. Please try again.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                elif sub_choice == '3':
                    # Go back to the main menu
                    break

        elif choice == '5':
            # Exit the program
            break


if __name__ == "__main__":
    main()
