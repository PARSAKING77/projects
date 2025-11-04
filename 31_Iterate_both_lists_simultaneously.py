lst1 = [10, 20, 30, 40]
lst2 = [100, 200, 300, 400]

for x, y in zip(lst1, lst2 [::-1]):

    print(x, y)