import random
import mysql.connector

class BankAccount:
    db = None
    cursor = None

    @staticmethod
    def connect_db():
        # Change these to match your MySQL account
        BankAccount.db = mysql.connector.connect(
            host="localhost",
            user="parsa",
            password="51849409790-Parsa_Soroush",
            database="bank",
            ssl_disabled=True
        )
        BankAccount.cursor = BankAccount.db.cursor()

        # Create table if not exists
        BankAccount.cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            age INT,
            credit_number VARCHAR(20),
            balance DECIMAL(15, 2) DEFAULT 0
        )
        """)
        BankAccount.db.commit()

    @staticmethod
    def option():
        print("Welcome to our Bank system😃. Please select an option:")
        print("1. Create Bank Account🏦")
        print("2. Deposit Money💸")
        userInput = input("Enter your choice: ")

        if userInput == "1":
            BankAccount.create_account()
        elif userInput == "2":
            BankAccount.deposit()
        else:
            print("Invalid option😉")

    @staticmethod
    def create_account():
        firstName = input("Please add your first name: ")
        lastName = input("Please add your last name: ")
        age = int(input("Please add your age: "))

        creditNumber = ''.join(str(random.randint(0, 9)) for _ in range(16))
        space = ' '.join(creditNumber[i:i+4] for i in range(0, 16, 4))

        if age <= 18:
            print("Sorry, you are not eligible to create a bank account😉")
        else:
            # Save to DB
            BankAccount.cursor.execute(
                "INSERT INTO accounts (first_name, last_name, age, credit_number) VALUES (%s, %s, %s, %s)",
                (firstName, lastName, age, space)
            )
            BankAccount.db.commit()

            print("Your Account created successfully😃")
            print("Here are your informations:")
            print(f"Your credit number is: {space}")
            print(f"Your first name is: {firstName}")
            print(f"Your last name is: {lastName}")
            print(f"Your age is: {age}")
            print("Your initial balance is: 0.00")

    @staticmethod
    def deposit():
        creditNumber = input("Enter your credit number: ")
        amount = float(input("Enter amount to deposit: "))

        # Check if account exists
        BankAccount.cursor.execute(
            "SELECT balance FROM accounts WHERE credit_number = %s", (creditNumber,)
        )
        result = BankAccount.cursor.fetchone()

        if result:
            new_balance = float(result[0]) + amount
            BankAccount.cursor.execute(
                "UPDATE accounts SET balance = %s WHERE credit_number = %s",
                (new_balance, creditNumber)
            )
            BankAccount.db.commit()
            print(f"Deposit successful! New balance: {new_balance:.2f}")
        else:
            print("Account not found!")

    
    @stat

# Main Execution
BankAccount.connect_db()
BankAccount.option()