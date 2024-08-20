n = int(input())
laptops = []
for _ in range(n):
    price, quality = map(int, input().split())
    laptops.append((price, quality))

laptops.sort()
for i in range(n-1):
    if laptops[i][1] > laptops[i+1][1]:
        print("happy irsa")
        break
else:
    print("poor irsa")