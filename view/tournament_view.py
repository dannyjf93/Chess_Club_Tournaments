class TournamentView:
    # Display message when there are no in progress tournaments available
    def display_no_in_progress_tournaments_message(self):
        print("There are no in progress tournaments available.")

    # Display message when there are no completed tournaments available
    def display_no_completed_tournaments_message(self):
        print("There are no completed tournaments available.")

    # Display list of in-progress tournaments
    def display_in_progress_tournaments(self, tournaments):
        print("\nIn-Progress Tournaments:")
        for index, tournament in enumerate(tournaments, start=1):
            print(f"{index}. {tournament.name} (Start Date: {tournament.start_date}, End Date: {tournament.end_date})")

    # Display list of completed tournaments
    def display_completed_tournaments(self, tournaments):
        print("\nCompleted Tournaments:")
        for index, tournament in enumerate(tournaments, start=1):
            print(f"{index}. {tournament.name} (Start Date: {tournament.start_date}, End Date: {tournament.end_date})")

    # Display prompt for selecting a tournament to manage
    def display_tournament_selection_prompt(self):
        print("Enter the number of the tournament to manage or 'b' to go back:")

    # Display detailed information about a selected tournament
    def display_tournament_details(self, tournament):
        print(f"\nTournament: {tournament.name}")
        print(f"Venue: {tournament.venue}")
        print(f"Start Date: {tournament.start_date}")
        print(f"End Date: {tournament.end_date}")

        # Show current round information if the tournament is in progress
        if not tournament.is_completed():
            print(f"Current Round: {tournament.current_round} of {tournament.number_of_rounds}\n")
        else:
            # Show total rounds played if the tournament is completed
            print(f"Rounds Played: {tournament.number_of_rounds}\n")

        # Display finished matches with their results
        print("Finished Matches:")
        for round_number, matches in tournament.results.items():
            print(f"Round {round_number}:")
            for match in matches:
                if match.get('draw'):
                    # If the match was a draw
                    print(f"Match: {match['player1']} (ID: {match['player1_id']})"
                          f" vs {match['player2']} (ID: {match['player2_id']}) - Draw")
                else:
                    # If there was a winner and loser
                    print(f"Match: {match['winner']} (ID: {match['winner_id']})"
                          f" defeated {match['loser']} (ID: {match['loser_id']})")

        # Display list of players sorted by score in descending order
        print("\nPlayers:")
        sorted_players = sorted(
            tournament.players, key=lambda player: tournament.scores[player['identifier']], reverse=True)
        rank = 1
        previous_score = None
        same_rank_count = 0
        for index, player in enumerate(sorted_players):
            current_score = tournament.scores[player['identifier']]
            if current_score != previous_score:
                rank = index + 1 - same_rank_count
                same_rank_count = 0
            else:
                same_rank_count += 1
            club = player.get('club', 'No club')
            place = self.ordinal(rank)
            print(f"{place} place: {player['name']} (ID: {player['identifier']})"
                  f" - Club: {club}, Score: {tournament.scores[player['identifier']]}")
            previous_score = current_score

    # Display prompt for entering match result
    def display_prompt_for_match_result(self, match, match_index):
        print(f"Match {match_index + 1}:")
        print(f"1. {match['player1']} (ID: {match['player1_id']}) wins")
        print(f"2. {match['player2']} (ID: {match['player2_id']}) wins")
        print("3. Draw")

    # Display message for invalid choice
    def display_invalid_choice_message(self):
        print("Invalid choice. Please try again.")

    # Convert a number to its ordinal representation (e.g., 1 -> 1st, 2 -> 2nd)
    @staticmethod
    def ordinal(n):
        return "%d%s" % (n, "tsnrhtdd"[(n // 10 % 10 != 1) * (n % 10 < 4) * n % 10::4])
