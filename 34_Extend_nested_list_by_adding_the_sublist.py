lst = ["a", "b",["c",["d","e",["f","g",],"k"],"l"],"m","n"]
lst2 = ["h","i","j"]

lst[2][1][2].extend(lst2)

print(lst)