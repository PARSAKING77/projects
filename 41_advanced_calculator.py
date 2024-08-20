def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operator():
    while True:
        operator = input("Enter operator (+, -, *, /): ")
        if operator in ['+', '-', '*', '/']:
            return operator
        else:
            print("Invalid operator. Please enter one of +, -, *, /.")

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero.")
            return None

def get_next_step():
    while True:
        choice = input("Do you want to (1) get the result or (2) perform another operation with the result? Enter 1 or 2: ")
        if choice in ['1', '2']:
            return choice
        print("Invalid option. Please enter 1 or 2.")

def get_followup_operator():
    while True:
        choice = input("Do you want to (1) add, (2) subtract, or (3) multiply with the previous result? Enter 1, 2, or 3: ")
        if choice in ['1', '2', '3']:
            return choice
        print("Invalid option. Please enter 1, 2, or 3.")

def main():
    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        operator = get_operator()

        result = calculate(num1, num2, operator)
        if result is None:
            continue

        print(f"Result: {result}")

        while True:
            next_step = get_next_step()
            if next_step == '1':
                print(f"Final result: {result}")
                break
            elif next_step == '2':
                followup_operator = get_followup_operator()
                num3 = get_number("Enter the number: ")
                if followup_operator == '1':
                    result += num3
                elif followup_operator == '2':
                    result -= num3
                elif followup_operator == '3':
                    result *= num3
                print(f"Updated result: {result}")

if __name__ == "__main__":
    main()