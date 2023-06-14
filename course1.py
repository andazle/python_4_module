import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='

today = datetime.today().strftime('%d/%m/%Y')
url = url + str(today)

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

id = input()
def get_course(id):
    print("1 шт.)", "стоит(ят)", soup.find('valute', {'id': id}).value.text)
    print(soup.find('name', {'id': id}).text)


get_course(input())

#print(soup)