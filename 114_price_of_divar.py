import requests
from bs4 import BeautifulSoup

# Send a GET request to the first page of Divar website
url = "https://divar.ir/s/tehran"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all ads with "قیمت توافقی" tag
ads_with_negotiable_price = []
for ad in soup.find_all('div', class_='kt-post-card'):
    for tag in ad.find_all('span', class_='kt-tag'):
        if tag.text.strip() == "قیمت توافقی":
            ads_with_negotiable_price.append(ad)

# Print the extracted ads
for ad in ads_with_negotiable_price:
    title = ad.find('h2', class_='kt-post-title').text.strip()
    price = ad.find('span', class_='kt-price').text.strip()
    print(f"Title: {title}, Price: {price}")