def calculte_average(numbers):

    float_nums = [float(num) for num in numbers]

    total = sum(float_nums)

    avg = total / len(float_nums)

    return avg


input_nums = ['21', '12']

res = calculte_average(input_nums)

print("Result:", res)