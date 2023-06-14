import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='

today = datetime.today().strftime('%d/%m/%Y')
url = url + today

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')


def get_course(id):
    """Добыча стоимости валюты. """
    return soup.find('valute', {'id': id}).value.text


print(get_course('R01235'), 'рублей за доллар')
print(get_course('R01239'), 'рублей за евро')
print(get_course('R01375'), 'рублей за юань')




