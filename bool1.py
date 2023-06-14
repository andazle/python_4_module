import requests
from pprint import pprint

url = 'https://swapi.dev/api/'

response = requests.get(url).json()

people = response.get('people')
planet = response['planets']
starships = response['starships']
#print(response)
#print(people)
#print(planet)
#print(starships)
def check_people(url):
    for i in range(1, 6):
        response = requests.get(f'{url}/{i}').json()
        pprint(response, sort_dicts=False)
        print()

def check_planets(url):
    diametrs_list = []
    for i in range(1, 6):
        response = requests.get(f'{url}/{i}').json()
        dictionary = {response.get('name'):response.get('diameter')}
        diametrs_list.append(dictionary)
    pprint(diametrs_list, sort_dicts=False)

check_people(people)
check_planets(planet)