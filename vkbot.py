import vk_api
from vk_bot import course
import requests


url = 'https://swapi.dev/api/'

response = requests.get(url).json()

planet = response.get('planets')

def check_planet(url):
    planet_diametr = 0
    planet_name = ''
    planets = []
    for i in range(2, 38):
        response = requests.get(f'{url}/{i}').json()
        dictionary = {'planet': response.get('name'),
                      'diametr': response.get('diameter')}
        planets.append(dictionary)
    for elem in planets:
        if int(elem['diametr']) > planet_diametr:
            planet_name = elem['planet']
    print(planet_name)


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


token='vk1.a.d_tnFCD1aA7CgxtjnwU3f3gIyuFOidxt5nGFonKA_E3LkG1nxDrAXT4aWPPlT7RYNCP6O-l8WGmTUb6KE-fqgHSfMbcv167h8O1Aos-dYb3swFjiKAz4UwFxf_4oyGAOTe9lHzBsUs5pBcA7I26s5zPVJoAKtqPj5EsPJRs-DXra8RAQ4kgHglooDMlmyWLHL5-NYfudYD51QVXIgwEfSQ'

vk = vk_api.VkApi(token=token)

vk._auth_token()
while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    if messages['count'] >= 1:
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']
        message_text = messages['items'][0]['last_message']['text']
        if message_text.lower() == 'курс доллара':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': f'Курс доллара: {course.get_course("R01235")}'})
        if message_text.lower() == 'планеты':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': f'Самая большая планета: {check_planet(planet)}'})
        if message_text.lower() == 'корабли':
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': f'Самая большая планета: {check_starships(starships)}'})
        else:
            vk.method('messages.send', {'peer_id': user_id, 'random_id': message_id, 'message': 'неизвестная команда'})

