def process_expression(expression):
    expression = expression.replace('+', ' ')  
    nums = list(map(int, expression.split()))  
    nums.sort()  

    result = ''
    ones = 0
    twos = 0
    threes = 0

    for num in nums:
        if num == 1:
            ones += 1
        elif num == 2:
            twos += 1
        else:
            threes += 1

    result += '1+' * ones + '2+' * twos + '3+' * threes

    return result

expression = input("")
print(process_expression(expression))