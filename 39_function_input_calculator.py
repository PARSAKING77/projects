def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def subtract(x, y):
    return x - y

def divid(x, y):
    return x / y

operation = {
    '+': add,
    '*': multiply,
    '-': subtract,
    '/': divid
}

def calculat(operator, x, y):
    return operation[operator](x, y)

opertor = input("Enter a operator (+, -, *, /):")
x = float(input("Enter first number: "))
y = float(input("Enter secend number: "))

res = calculat(opertor, x, y)

print("Result: ", res)