import requests

def scrape(url):
    req = requests.get(url)
    with open('out.html', 'w') as f:
        f.write(req.text)