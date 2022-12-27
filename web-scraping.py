import requests
from bs4 import BeautifulSoup
import csv

date = input(
    'Enter a date for the matches you want to see, following this format MM/DD/YY: ')
page = requests.get(f'https://www.yallakora.com/match-center/?date={date}')


def gettingMatchesData(page):
    soup = BeautifulSoup(page.content, 'lxml')
    print(soup)


gettingMatchesData(page)
