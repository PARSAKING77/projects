def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return "not prime"
        else:
            return "prime"
    else:
        return "not prime"

number = int(input("Enter a positive number: "))


print(is_prime(number))
