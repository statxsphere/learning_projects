from bs4 import BeautifulSoup
import requests

years = list(range(2011,2019))
file = requests.get("http://www.tankathon.com/past_drafts/2018").text
soup = BeautifulSoup(file, 'lxml')
l = []

for match_adv in soup.find_all('div', class_='stats-advanced'):
    try:
        match_usg = match_adv.find('div', class_='stat reb')
        match1 = match_usg.find('div')
        match2 = match_usg.find('div', class_='label')
        if match_usg:
            l.append(match1.text)

    except:
        l.append(None)
print(l)

