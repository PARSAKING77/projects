list1 = ["M", "na", "i", "pa"] 
list2 = ["y", "me", "s", "rsa"]

lst3 = [i + j for i, j in zip(list1, list2)]

print(lst3)