from bs4 import BeautifulSoup
import requests
import pandas as pd


years = list(range(2011,2019))
name = []
position = []
pick = []
height = []
weight = []
c_year = []
age = []
points = []
rebounds = []
assists = []
steals = []
blocks = []
TS = []
usg = []
obp = []
dbp = []
final = pd.DataFrame()

file = requests.get(f"http://www.tankathon.com/past_drafts/2018").text
soup = BeautifulSoup(file, 'lxml')


def collect_singleyr_stats(year):
    file = requests.get(f"http://www.tankathon.com/past_drafts/{str(year)}").text
    soup = BeautifulSoup(file, 'lxml')
    # name
    for names in soup.find_all('div', class_='mock-row-name'):
        name.append(names.text)

    # position
    for positions in soup.find_all('div', class_='mock-row-school-position'):
        position.append(positions.text[0:2].rstrip())

    #pick
    for picks in soup.find_all('div', class_='mock-row-pick-number'):
        pick.append(picks.text)

    # measurements
    for measurements in soup.find_all('div', class_='section height-weight'):
        # print(measurements)
        a = measurements.text.split('"')
        height.append(a[0])
        weight.append(a[1])

    #age
    for i in soup.find_all('div', class_='section year-age desktop'):
        x = i.find_all('div')
        c_year.append(x[0].text)
        age.append(x[1].text)

    # per-36
    for match_36 in soup.find_all('div', class_='stats-per-36'):
        try:
            point = match_36.find('div', class_='stat pts')
            match1 = point.find('div')
            points.append(match1.text)
        except:
            points.append(None)

        try:
            reb = match_36.find('div', class_='stat reb')
            match2 = reb.find('div')
            rebounds.append(match2.text)
        except:
            rebounds.append(None)

        try:
            ast = match_36.find('div', class_='stat ast')
            match3 = ast.find('div')
            assists.append(match3.text)
        except:
            assists.append(None)

        try:
            stl = match_36.find('div', class_='stat stl desktop')
            match4 = stl.find('div')
            steals.append(match4.text)
        except:
            steals.append(None)

        try:
            blk = match_36.find('div', class_='stat blk desktop')
            match5 = blk.find('div')
            blocks.append(match5.text)
        except:
            blocks.append(None)

    for match_adv in soup.find_all('div', class_='stats-advanced'):
        try:
            TSp = match_adv.find('div', class_='stat pts')
            match6 = TSp.find('div')
            TS.append(match6.text)
        except:
            TS.append(None)

        try:
            usage = match_adv.find('div', class_='stat reb')
            match7 = usage.find('div')
            usg.append(match7.text)
        except:
            usg.append(None)

        try:
            bpo = match_adv.find('div', class_='stat ast')
            match8 = bpo.find('div')
            obp.append(match8.text)
        except:
            obp.append(None)

        try:
            bpd = match_adv.find('div', class_='stat stl desktop')
            match9 = bpd.find('div')
            dbp.append(match9.text)
        except:
            dbp.append(None)


