class Tournament:
    def __init__(self, name, venue, start_date, end_date, number_of_rounds):
        # Initialize tournament attributes
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.current_round = 1
        self.players = []
        self.scores = {}
        self.results = {}
        self.completed = False

    # Check if the tournament is completed
    def is_completed(self):
        return self.completed

    # Convert tournament object to dictionary
    def to_dict(self):
        return {
            'name': self.name,
            'venue': self.venue,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'number_of_rounds': self.number_of_rounds,
            'current_round': self.current_round,
            'players': self.players,
            'scores': self.scores,
            'results': self.results,
            'completed': self.completed
        }

    # Create a tournament object from a dictionary
    @classmethod
    def from_dict(cls, data):
        # Instantiate a tournament object using data from the dictionary
        tournament = cls(
            data['name'],
            data['venue'],
            data['start_date'],
            data['end_date'],
            data['number_of_rounds']  # Ensure number_of_rounds is required and present
        )
        # Set additional attributes using data from the dictionary
        tournament.current_round = data.get('current_round', 1)
        tournament.players = data.get('players', [])
        tournament.scores = data.get('scores', {})
        tournament.results = data.get('results', {})
        tournament.completed = data.get('completed', False)
        return tournament
