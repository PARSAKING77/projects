import random
import mysql.connector

class BankAccount:
    db = None
    cursor = None

    @staticmethod
    def connect_db():
        # Change these to your real MySQL account info
        BankAccount.db = mysql.connector.connect(
            host="localhost",  # Your MySQL host
            user="parsa",            # Your MySQL username
            password="51849409790-",        # Your MySQL password
            database="your_database_name",   # Your MySQL database
            port=3306                         # Your MySQL port
        )
        BankAccount.cursor = BankAccount.db.cursor()

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
