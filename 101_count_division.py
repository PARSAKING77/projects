def count_prime_divisors(n):
    count = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if is_prime(i):
                count += 1
            if i != n // i and is_prime(n // i):
                count += 1
    if is_prime(n):
        count += 1
    return count

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = []
for _ in range(10):
    numbers.append(int(input()))

max_divisors = 0
max_number = 0
for num in numbers:
    divisors = count_prime_divisors(num)
    if divisors > max_divisors:
        max_divisors = divisors
        max_number = num
    elif divisors == max_divisors:
        max_number = max(max_number, num)

print(max_number, max_divisors)