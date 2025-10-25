class Player:
    def __init__(self, playerName, playerPosition):
        self.playerName = playerName
        self.playerPosition = playerPosition

    def __str__(self):
        return f"{self.playerName} ({self.playerPosition})"

class NFLTeam:
    def __init__(self, teamName, players=None):
        self.teamName = teamName
        self.players = players if players is not None else []

    def add_player(self, player):
        self.players.append(player)

    def print_team(self):
        print(f"Team Name: {self.teamName}")
        print("Players:")
        for p in self.players:
            print(f"  {p}")

player1 = Player("Alex Barnett ", "Quarterback")
player2 = Player("John Marshall", "Running Back")
player3 = Player("Wes Sapp", "Wide Receiver")
player4 = Player("Jack Hefley", "Kicker")

playerList = [player1, player2, player3, player4]

team = NFLTeam("Bluffs Blue Jays", playerList)

team.print_team()