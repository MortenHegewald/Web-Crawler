import requests
from bs4 import BeautifulSoup
import csv

def spider(max_pages):
    page = 0
    file = open("teams.txt", "w")
    while page <= max_pages:
        url = 'http://www.espn.com/college-football/teams'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        for item in soup.findAll('div', {'class': 'span-2'}):
            for league in item.findAll('div', {'class': 'mod-container mod-open-list mod-teams-list-medium mod-no-footer'}):
                for leaguename in league.findAll('div', {'class': 'mod-header colhead'}):
                    for leg in leaguename.findAll('h4'):
                        print("#######LEAGE NAME:" + leg.string + "######")
                        file.write("#######LEAGE NAME:" + leg.string + "######" '\n')
                for teamname in league.findAll('a', {'class': 'bi'}):
                    print(teamname.string)
                    file.write(teamname.string + '\n')

        page = page + 1
    file.close()


spider(1)
