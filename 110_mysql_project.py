import mysql.connector

# Establish a connection to the MySQL server
cnx = mysql.connector.connect(
    user='root',
    password='',
    host='localhost'
)

# Create a new database
cursor = cnx.cursor()
cursor.execute("CREATE DATABASE employee_db")
cnx.database = "employee_db"

# Create a new table
cursor.execute("""
    CREATE TABLE employees (
        Name VARCHAR(50),
        Height INT,
        Weight INT
    )
""")
cnx.commit()

# Insert sample data into the table
employees = [
    ("Amin", 180, 75),
    ("Mahdi", 190, 90),
    ("Mohammad", 175, 75),
    ("Ahmad", 175, 60)
]
cursor.executemany("INSERT INTO employees (Name, Height, Weight) VALUES (%s, %s, %s)", employees)
cnx.commit()

# Read data from the table and print employees in order of height and weight
cursor.execute("SELECT * FROM employees ORDER BY Height DESC, Weight ASC")
employees = cursor.fetchall()

for employee in employees:
    print(f"{employee[0]} {employee[1]} {employee[2]}")

# Close the cursor and connection
cursor.close()
cnx.close()