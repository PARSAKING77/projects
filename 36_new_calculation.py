input_string = input("Enter two numbers and an operator (for exampel: 5 + 10: ")

input_list = input_string.split()
num1 = float(input_list[0])
operator = input_list[1]
num2 = float(input_list[2])

result = None
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero!")
else:
    print("Error: Invalid operator!")

if result is not None:
    print(f"{num1} {operator} {num2} = {result}")