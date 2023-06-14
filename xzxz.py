import webbrowser
import pyttsx3
import speech_recognition as sr
import random

r = sr.Recognizer()
voice = pyttsx3.init()
voice.say('Привет, я твой голосовой помощник')
voice.runAndWait()
spisok = ['здравствуйте', 'салют', 'кого я вижу', 'мир вашему дому', 'сердечно приветствую вас', 'рад встрече с вами', 'приятно снова вас видеть']
film = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
while True:
    with sr.Microphone(device_index=0) as source:
        print('Скажите что нибудь')
        audio = r.listen(source)

    speech = r.recognize_google(audio, language='ru_RU').lower()
    print('Высказали:', speech)

    if speech.find('привет') >= 0:
        voice.say(random.choice(spisok))
        voice.runAndWait()
    elif speech.find('пока') >= 0:
        voice.say('пока')
        voice.runAndWait()
        break
    elif speech.find('яндекс') >= 0:
        webbrowser.open_new('https://ya.ru/')
        voice.say('Яндекс открыт')
        voice.runAndWait()
    elif speech.find('Фильм') >= 0:
        voice.say(f'Рекомендую вам {random.choice(film)}')
        voice.runAndWait()
    else:
        voice.say('я вас не понимаю')
        voice.runAndWait()

