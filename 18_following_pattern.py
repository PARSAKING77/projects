num = 5
for x in range(0, num):
    for y in range(0, x + 1):
        print("*", end=' ')
    print("\r")

for x in range(num, 0, -1):
    for y in range(0, x - 1):
        print("*", end=' ')
    print("\r")