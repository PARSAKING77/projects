max_age = -1
secende_max_age = -1

while True:

    age = int(input())

    if age == -1:
        break

    if age < 10 or age > 90:
        print("the age coulde be in 10 years old to 90 years old")
        continue

    if age > max_age:
        secende_max_age = max_age
        max_age = age
    elif age > secende_max_age:
        secende_max_age = age

print(max_age, secende_max_age)