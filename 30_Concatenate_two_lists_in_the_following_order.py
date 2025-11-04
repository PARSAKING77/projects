list1 = ["hello ", "take "]
list2 = ["dear", "sir"]

p = [x + y for x in list1 for y in list2]

print(p)