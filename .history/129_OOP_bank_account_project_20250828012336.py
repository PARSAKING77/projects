import random
import mysql.connector

class BankAccount:
    db = None
    cursor = None
    # Define withdrawal limit per transaction
    WITHDRAWAL_LIMIT = 100.00

    @staticmethod
    def connect_db():
        BankAccount.db = mysql.connector.connect(
            host="localhost",
            user="parsa",
            password="51849409790-Parsa_Soroush",
            database="bank",
            ssl_disabled=True
        )
        BankAccount.cursor = BankAccount.db.cursor()

        BankAccount.cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            age INT,
            credit_number VARCHAR(20),
            account_type ENUM('saving','checking') DEFAULT 'checking',
            balance DECIMAL(15, 2) DEFAULT 0
        )
        """)
        BankAccount.db.commit()

    @staticmethod
    def option():
        print("Welcome to our Bank system😃. Please select an option:")
        print("1. Create Bank Account🏦")
        print("2. Deposit Money💸")
        print("3. Withdraw Money💰")
        print("4. Check Account Type🔎")
        userInput = input("Enter your choice: ")

        if userInput == "1":
            BankAccount.create_account_with_type()
        elif userInput == "2":
            BankAccount.deposit()
        elif userInput == "3":
            BankAccount.withdraw()
        elif userInput == "4":
            BankAccount.check_account_type()
        else:
            print("Invalid option😉")

    @staticmethod
    def create_account_with_type():
        firstName = input("Please add your first name: ")
        lastName = input("Please add your last name: ")
        age = int(input("Please add your age: "))

        # Choose account type
        print("Select Account Type: ")
        print("1. Saving Account (Monthly interest, limited withdrawal)")
        print("2. Checking Account (No interest, free withdrawal)")
        account_choice = input("Enter your choice: ")

        if account_choice == "1":
            account_type = "saving"
        else:
            account_type = "checking"

        # Generate 16-digit credit number
        creditNumber = ''.join(str(random.randint(0, 9)) for _ in range(16))
        space = ' '.join(creditNumber[i:i+4] for i in range(0, 16, 4))

        if age <= 18:
            print("Sorry, you are not eligible to create a bank account😉")
        else:
            # Insert account into DB
            BankAccount.cursor.execute(
                "INSERT INTO accounts (first_name, last_name, age, credit_number, account_type) VALUES (%s, %s, %s, %s, %s)",
                (firstName, lastName, age, space, account_type)
            )
            BankAccount.db.commit()

            # Display user info
            print("Your Account created successfully😃")
            print("Here are your informations:")
            print(f"Your credit number is: {space}")
            print(f"Your first name is: {firstName}")
            print(f"Your last name is: {lastName}")
            print(f"Your age is: {age}")
            print(f"Your account type is: {account_type}")
            print("Your initial balance is: 0.00")
            print(f"Withdrawal limit per transaction: {BankAccount.WITHDRAWAL_LIMIT:.2f}")

    @staticmethod
    def deposit():
        creditNumber = input("Enter your credit number: ")
        amount = float(input("Enter amount to deposit: "))

        # Validate positive amount
        if amount <= 0:
            print("Deposit amount must be positive!")
            return

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

    @staticmethod
    def withdraw():
        sender_card = input("Please enter the sender's card number: ")
        receiver_card = input("Enter the receiver's card number: ")
        amount = float(input("Please enter the Amount: "))

        # Check withdrawal limit for each transaction
        if amount > BankAccount.WITHDRAWAL_LIMIT:
            print(f"Withdrawal limit exceeded!")
            print(f"Maximum withdrawal per transaction: {BankAccount.WITHDRAWAL_LIMIT:.2f}")
            print(f"Requested amount: {amount:.2f}")
            print("Transaction cancelled.")
            return

        # Validate positive amount
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return

        # Check if sender exists and get balance + type
        BankAccount.cursor.execute(
            "SELECT balance, account_type FROM accounts WHERE credit_number = %s", (sender_card,)
        )
        sender_result = BankAccount.cursor.fetchone()

        if not sender_result:
            print("Sender account not found!")
            return

        sender_balance = float(sender_result[0])
        sender_type = sender_result[1]

        # Check balance
        if sender_balance < amount:
            print("Insufficient balance in sender's account!")
            print(f"Available balance: {sender_balance:.2f}")
            print(f"Requested amount: {amount:.2f}")
            return

        # Additional restriction for saving accounts (if needed)
        if sender_type == "saving" and amount > 50.00:
            print("Saving account has additional withdrawal restriction!")
            print("Maximum withdrawal for saving accounts: 50.00 per transaction")
            return

        # Check if receiver exists
        BankAccount.cursor.execute(
            "SELECT balance FROM accounts WHERE credit_number = %s", (receiver_card,)
        )
        receiver_result = BankAccount.cursor.fetchone()

        if not receiver_result:
            print("Receiver account not found!")
            return

        receiver_balance = float(receiver_result[0])

        # Update balances
        new_sender_balance = sender_balance - amount
        new_receiver_balance = receiver_balance + amount

        BankAccount.cursor.execute(
            "UPDATE accounts SET balance = %s WHERE credit_number = %s",
            (new_sender_balance, sender_card)
        )
        BankAccount.cursor.execute(
            "UPDATE accounts SET balance = %s WHERE credit_number = %s",
            (new_receiver_balance, receiver_card)
        )

        BankAccount.db.commit()
        print("Withdrawal successful!")
        print(f"{amount:.2f} transferred from {sender_card} to {receiver_card}")
        print(f"Sender's new balance: {new_sender_balance:.2f}")
        print(f"Receiver's new balance: {new_receiver_balance:.2f}")

    @staticmethod
    def check_account_type():
        """Ask for credit card and show account type + balance"""
        creditNumber = input("Enter your credit number: ")

        BankAccount.cursor.execute(
            "SELECT first_name, last_name, account_type, balance FROM accounts WHERE credit_number = %s", (creditNumber,)
        )
        result = BankAccount.cursor.fetchone()

        if result:
            first_name, last_name, account_type, balance = result
            print(f"Account Holder: {first_name} {last_name}")
            print(f"Account Type: {account_type}")
            print(f"Current Balance: {balance:.2f}")
            print(f"Withdrawal limit per transaction: {BankAccount.WITHDRAWAL_LIMIT:.2f}")
        else:
            print("Account not found!")

    @staticmethod
    def show_withdrawal_limits():
        """Display withdrawal limits"""
        print("\nWithdrawal Limits:")
        print(f"• General withdrawal limit: {BankAccount.WITHDRAWAL_LIMIT:.2f} per transaction")
        print("• Saving accounts: 50.00 per transaction (additional restriction)")
        print("• Checking accounts: 100.00 per transaction")

# Main Execution
if __name__ == "__main__":
    BankAccount.connect_db()
    
    # Display limits at the beginning of the program
    BankAccount.show_withdrawal_limits()
    
    while True:
        BankAccount.option()
        
        continue_choice = input("\nDo you want to perform another operation? (y/n): ").lower()
        if continue_choice != 'y':
            print("Thank you for using our Bank System! 👋")
            break
    
    # Close database connection
    if BankAccount.db:
        BankAccount.db.close()