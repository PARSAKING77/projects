def find_oldest_candidate():
    max_age = 10

    while True:
        try:
            age = int(input(""))

            if age <0:
                break
            if 10<= age <= 90:
                max_age = max(max_age, age)

            else:
                print("Age shoulde be in range of 10 to 90 years.")

        except ValueError:
            print("Please enter a valid integer.")

    print(max_age)

find_oldest_candidate()

