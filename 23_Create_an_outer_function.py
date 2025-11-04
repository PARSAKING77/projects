def sum_num(a, b):
    square = a ** 2

    def addition(a, b):
        return a + b

    add = addition(a, b)
    return add + 5

result = sum_num(5, 10)
print(result)