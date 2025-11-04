import random
import m

class BankAccount:
    db = None
    cursor = None

    @staticmethod
    def connect_db():
        BankAccount.db = mysql.connector.connect(
            host="localhost",
            user="parsa",
            password="51849409790-Parsa_Soroush",
            database="bank",
            port=3306
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
