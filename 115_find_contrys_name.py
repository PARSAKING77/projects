import requests
from bs4 import BeautifulSoup
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('countries.db')
cursor = conn.cursor()

# Create a table to store the country data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY,
        name TEXT,
        capital TEXT,
        population INTEGER,
        area REAL
    )
''')

# Send a GET request to the website
url = "https://scrapethissite.com/pages/simple/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all country rows
country_rows = soup.find_all('tr')[1:21]  # Extract the first 20 countries

# Extract and store the country data
for row in country_rows:
    columns = row.find_all('td')
    name = columns[0].text.strip()
    capital = columns[1].text.strip()
    population = int(columns[2].text.strip().replace(',', ''))
    area = float(columns[3].text.strip().replace(',', ''))
    cursor.execute('''
        INSERT INTO countries (name, capital, population, area)
        VALUES (?, ?, ?, ?)
    ''', (name, capital, population, area))

# Commit the changes and close the connection
conn.commit()
conn.close()