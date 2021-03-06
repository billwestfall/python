from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://en.wikipedia.org'

HEADERS = {'User-Agent': 'Mozilla/5.0'}

def get_Nobel_soup():
    response = requests.get(BASE_URL + '/wiki/List_of_Nobel_laureates' + headers=HEADERS)
    soup =  BeautifulSoup(response.content, "lxml")

print(soup)
