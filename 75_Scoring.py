points = 0
wins = 0


for _ in range(30):

    p = int(input(""))
    points += p

    if p == 3:
        wins += 1


print(points, wins)