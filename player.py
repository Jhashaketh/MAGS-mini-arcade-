class Player:
    def __init__(self, username):
        self.username = username
        self.games_played = 0
        self.wins = 0
        self.losses = 0

    def record_win(self):
        self.wins += 1
        self.games_played += 1

    def record_loss(self):
        self.losses += 1
        self.games_played += 1

    def get_stats(self):
        return f"Games: {self.games_played}, Wins: {self.wins}, Losses: {self.losses}"

    def to_dict(self):
        return {
            "games_played": self.games_played,
            "wins": self.wins,
            "losses": self.losses
        }


    def from_dict(username, data):
        p = Player(username)
        p.games_played = data["games_played"]
        p.wins = data["wins"]
        p.losses = data["losses"]
        return p