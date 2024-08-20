n = int(input())
players = list(map(int, input().split()))
players.sort(reverse=True)

teams = 0
i = 0
while i < n:
    if players[i] <= 2:
        teams += 1
        i += 3
    else:
        i += 1

print(teams)