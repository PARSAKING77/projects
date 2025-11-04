import random

class Human:
    def __init__(self, name):
        self.name = name

class FootballPlayer(Human):
    def __init__(self, name):
        super().__init__(name)
        self.team = None

players = [FootballPlayer(name) for name in ["حسین", "مازیار", "اکبر", "نیما", "مهدی", "فرهاد", "محمد", 
"خشایار", "میلاد", "مصطفی", "امین", "سعید", "پویا", "پوریا", "رضا", "علی", "بهزاد", "سهیل", "بهروز", "شهروز", "سامان", "محسن"]]

random.shuffle(players)

team_a = players[:11]
team_b = players[11:]

for player in team_a:
    player.team = "A"

for player in team_b:
    player.team = "B"

for player in players:
    print(f"{player.name} - Team {player.team}")