import requests
from bs4 import BeautifulSoup
import csv


def gettingMatchesData(page):
    soup = BeautifulSoup(page.content, 'lxml')
    championships = soup.find_all('div', {'class': 'matchCard'})
    matchDetails = []
    for championship in championships:
        championshipTitle = championship.find('h2').text.strip()
        championshipMatches = championship.find_all('li', {'class': 'item'})
        for match in championshipMatches:
            teamA = match.find('div', {'class': 'teamA'}).text.strip()
            teamB = match.find('div', {'class': 'teamB'}).text.strip()
            matchResult = match.find_all('span', {'class': 'score'})
            matchTime = match.find('span', {'class': 'time'}).text.strip()
            matchStatus = match.find('span', {'class': 'status'}).text.strip()

            matchDetails.append({'الفريق الأول': teamA, 'نتيجة المباراة': f'{matchResult[0].text.strip()} - {matchResult[1].text.strip()}', 'الفريق الثانى': teamB,
                                 'وقت المباراة': matchTime, 'حالة المباراة': matchStatus, 'البطولة': championshipTitle})
    return matchDetails


def creatingCSVFile(data):
    keys = data[0].keys()
    with open('./matches.csv', 'w', encoding="utf-8") as outputFile:
        dictWriter = csv.DictWriter(outputFile, keys)
        dictWriter.writeheader()
        dictWriter.writerows(data)
        print('file created successfuly')


if __name__ == "__main__":
    date = input(
        'Enter a date for the matches you want to see, following this format MM/DD/YY: ')
    page = requests.get(f'https://www.yallakora.com/match-center/?date={date}')
    scrapedData = gettingMatchesData(page)
    creatingCSVFile(scrapedData)
