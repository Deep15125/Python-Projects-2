import requests
from bs4 import BeautifulSoup
import re 

def scrape_section_headings(url):
    response = requests.get(url)

    print("Response Status Code:", response.status_code)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        headings = soup.find_all(re.compile('^h[1-6]$'))

        for heading in headings:
            print(heading.text.strip())

    else:
        print("Failed to retrieve section heading")

url = 'https://github.com/Deep15125'

scrape_section_headings(url)