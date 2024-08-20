def count_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

numbers = []
for _ in range(20):
    num = int(input("Enter a number: "))
    numbers.append(num)

max_divisors = 0
max_number = 0
for num in numbers:
    divisors = count_divisors(num)
    if divisors > max_divisors:
        max_divisors = divisors
        max_number = num

print("The number with the highest number of divisors is", max_number, "with", max_divisors, "divisors.")