ages = []
while True:
    age = int(input("Enter the age of the candidate: "))
    if age < 0:
        break
    if age < 10 or age > 90:
        print("Invalid age. Age should be between 10 and 90.")
        continue
    ages.append(age)

if len(ages) < 2:
    print("At least two candidates are required to find the oldest and the second oldest.")
else:
    ages.sort()
    print("The oldest candidate is", ages[-1], "years old.")
    print("The second oldest candidate is", ages[-2], "years old.")_