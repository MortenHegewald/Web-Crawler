import requests
from bs4 import BeautifulSoup

def spider1(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.dba.dk/toej-og-mode/toej-til-maend/side-' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for link in soup.findAll('a', {'class': 'listingLink'}):
            href = link.get('href')
            title = link.string
            print(href)
            print(title)
            #get_single_item_data(href)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    for item_name in soup.findAll('h2', {'class': 'fn'}):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = link.get('href')
        print(href)




spider1(1)