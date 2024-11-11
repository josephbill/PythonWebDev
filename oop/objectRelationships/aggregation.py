class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)


class Player:
    def __init__(self, name):
        self.name = name


team = Team("Liverpool")
player1 = Player("Mo Salah")
team.add_player(player1)

print(team.players)

## Team aggregates players , players can exist independently of teams