import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from course import get_course
import random
from wiki import get_wiki_article

TOKEN='vk1.a.d_tnFCD1aA7CgxtjnwU3f3gIyuFOidxt5nGFonKA_E3LkG1nxDrAXT4aWPPlT7RYNCP6O-l8WGmTUb6KE-fqgHSfMbcv167h8O1Aos-dYb3swFjiKAz4UwFxf_4oyGAOTe9lHzBsUs5pBcA7I26s5zPVJoAKtqPj5EsPJRs-DXra8RAQ4kgHglooDMlmyWLHL5-NYfudYD51QVXIgwEfSQ'

vk_session = vk_api.VkApi(token=TOKEN)

vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
     if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        message = event.text.lower()
        user_id = event.user_id
        print(message, user_id)
        random_id = random.randint(1, 10 ** 10)
        if message == '-к доллар':
            response = f'{get_course("R01235")} рублей за доллар'
            vk.messages.send(user_id=user_id, random_id=random_id, message=response)
        if message == '-к юань':
            response = f'get_course("R01375") рублей за  юань'
            vk.messages.send(user_id=user_id, random_id=random_id, message=response)
        if message == '-к фунт стерлингов':
            response = f'get_course("R01035") рублей за фунт стерлингов'
            vk.messages.send(user_id=user_id, random_id=random_id, message=response)
        if message == '-к австралийский доллар':
            response = f'get_course("R01010") рублей за австралийский доллар'
            vk.messages.send(user_id=user_id, random_id=random_id, message=response)
        if message == '-к евро':
            response = f'{get_course("R01239")} рублей за евро'
            vk.messages.send(user_id=user_id, random_id=random_id, message=response)
        elif message.startswith('-в'):
            response = get_wiki_article(message[2:])
        else:
            response = 'Неизвестная команда'
        vk.messages.send(user_id=user_id, random_id=random_id, message=response)
