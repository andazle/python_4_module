import requests

url = 'https://swapi.dev/api/'

response = requests.get(url).json()

starships = response.get('starships')


def check_starships(url):
    starships_max_atmosphering_speed = 0
    starships_name = ''
    speed_starships = []
    for i in range(2, 12):
        response = requests.get(f'{url}/{i}').json()
        dictionary = {'name':response.get('name'),
                      'speed':response.get('max_atmosphering_speed')}
        speed_starships.append(dictionary)
    for elem in speed_starships:
        if elem['speed'] == None or elem['name'] == None:
            speed_starships.pop(speed_starships.index(elem))
        if int(elem['speed']) > starships_max_atmosphering_speed:
            starships_name = elem['name']
    print(starships_name)


check_starships(starships)