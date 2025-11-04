class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.loses = 0
        self.draws = 0
        self.goals_for = 0
        self.goals_against = 0
        self.points = 0

    def update_stats(self, goals_scored, goals_conceded):
        self.goals_for += goals_scored
        self.goals_against += goals_conceded
        if goals_scored > goals_conceded:
            self.wins += 1
            self.points += 3
        elif goals_scored < goals_conceded:
            self.loses += 1
        else:
            self.draws += 1
            self.points += 1

    def goal_difference(self):
        return self.goals_for - self.goals_against

    def __str__(self):
        return f"{self.name}  wins:{self.wins} , loses:{self.loses} , draws:{self.draws} , goal difference:{self.goal_difference()} , points:{self.points}"

teams = [
    Team("Iran"),
    Team("Spain"),
    Team("Portugal"),
    Team("Morocco")
]

matches = [
    (0, 1),  # Iran - Spain
    (0, 2),  # Iran - Portugal
    (0, 3),  # Iran - Morocco
    (1, 2),  # Spain - Portugal
    (1, 3),  # Spain - Morocco
    (2, 3)   # Portugal - Morocco
]


for match in matches:
    result = input().strip()
    score1, score2 = map(int, result.split('-'))
    team1, team2 = match
    teams[team1].update_stats(score1, score2)
    teams[team2].update_stats(score2, score1)


teams.sort(key=lambda x: (-x.points, -x.wins, x.name))

for team in teams:
    print(str(team))
