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
        pick.append(int(picks.text))

    # measurements
    for measurements in soup.find_all('div', class_='section height-weight'):
        a = measurements.text.split('"')
        heights = a[0].split("'")
        heights1 = int(heights[0]) * 12 + float(heights[1])
        height.append(round(heights1 * 2.54, 1))
        weight.append(int(a[1][0:4]))

    #age
    for i in soup.find_all('div', class_='section year-age desktop'):
        x = i.find_all('div')
        c_year.append(x[0].text)
        age.append(float(x[1].text[0:4]))

    # per-36
    for stats in soup.find_all('div', class_='mock-row-stats'):
        try:
            match_36 = stats.find('div', class_='stats-per-36')
            point = match_36.find('div', class_='stat pts')
            match1 = point.find('div')
            points.append(float(match1.text))
        except:
            points.append(None)

        try:
            match_36 = stats.find('div', class_='stats-per-36')
            reb = match_36.find('div', class_='stat reb')
            match2 = reb.find('div')
            rebounds.append(float(match2.text))
        except:
            rebounds.append(None)

        try:
            match_36 = stats.find('div', class_='stats-per-36')
            ast = match_36.find('div', class_='stat ast')
            match3 = ast.find('div')
            assists.append(float(match3.text))
        except:
            assists.append(None)

        try:
            match_36 = stats.find('div', class_='stats-per-36')
            stl = match_36.find('div', class_='stat stl desktop')
            match4 = stl.find('div')
            steals.append(float(match4.text))
        except:
            steals.append(None)

        try:
            match_36 = stats.find('div', class_='stats-per-36')
            blk = match_36.find('div', class_='stat blk desktop')
            match5 = blk.find('div')
            blocks.append(float(match5.text))
        except:
            blocks.append(None)

        try:
            match_adv = stats.find('div', class_='stats-advanced')
            TSp = match_adv.find('div', class_='stat pts')
            match6 = TSp.find('div')
            TS.append(float(match6.text))
        except:
            TS.append(None)

        try:
            match_adv = stats.find('div', class_='stats-advanced')
            usage = match_adv.find('div', class_='stat reb')
            match7 = usage.find('div')
            usg.append(float(match7.text))
        except:
            usg.append(None)

        try:
            match_adv = stats.find('div', class_='stats-advanced')
            bpo = match_adv.find('div', class_='stat ast')
            match8 = bpo.find('div')
            obp.append(float(match8.text))
        except:
            obp.append(None)

        try:
            match_adv = stats.find('div', class_='stats-advanced')
            bpd = match_adv.find('div', class_='stat blk desktop')
            match9 = bpd.find('div')
            dbp.append(float(match9.text))
        except:
            dbp.append(None)

def collect_all(years):
    for year in years:
        collect_singleyr_stats(year)