import telebot
import random


TOKEN = '5641455452:AAECIwKxQ9hCBRRautThUVgfAZ71XHOvWGQ'
bot = telebot.TeleBot(TOKEN)

def open_file(file_name):
    with open(f'./{file_name}', 'r') as f:
        list = f.readlines()
    return list

with opw
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('/continue', '/random_movie')
    bot.send_photo(message.from_user.id, 'https://i.pinimg.com/originals/99/03/2c/99032c3c5a7826f701501dd5af86f3c6.jpg', caption='Приветствую вас, дорогой пользовалтель! Я новогодний бот. Могу найти для вас фильм по актёру и жанру. Для этого вам нужно нажать на\n /continue\nТакже я могу предложить случайный фильм из своей базы. Для этого вам нужно нажать на\n /random_movie ', reply_markup=keyboard)


@bot.message_handler(commands=['random_movie'])
def random_movie(message):
    keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
    keyboard1.row('/continue', '/random_movie')
    random_movie2 = random.choice(open_file('film.txt'))
    random_movie3 = random_movie2.split(',')
    bot.send_message(
        message.from_user.id,
        f'Ваш случайный фильм - {random_movie3[1]} \n {random_movie3[-1]}')
    bot.send_message(
        message.from_user.id,
        'Чтобы найти новый фильм нажмите на /continue\nили чтобы получить случайный фильм нажмите /random_movie',
        reply_markup=keyboard1)


@bot.message_handler(commands=['continue'])
def continue_1(message):
    bot.send_message(message.from_user.id,
                     'Для выбора актера отправьте в чат его номер:\n' +
                     ''.join(open_file('actor.txt')),
                     reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, select_actor)


temporary_actor = ''


def select_actor(message):
    keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
    keyboard2.row('/next')
    global temporary_actor
    if message.text.isdigit():
        temporary_actor = open_file('actor.txt')[int(message.text) - 1]
        temporary_actor = temporary_actor.split()[-1]
    if temporary_actor:
        bot.send_message(message.from_user.id,
                         'Нажмите /next чтобы выбрать жанр',
                         reply_markup=keyboard2)


@bot.message_handler(commands=['next'])
def next(message):
    bot.send_message(
        message.from_user.id,
        'Для выбора жанра отправьте в чат его номер:\n' + ''.join(open_file('genres.txt')),
    reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.register_next_step_handler(message, select_genre)


def select_genre(message):
    keyboard4 = telebot.types.ReplyKeyboardMarkup(True)
    keyboard4.row('/end')
    global temporary_genre
    if message.text.isdigit():
        temporary_genre = open_file('genres.txt')[int(message.text) - 1]
        temporary_genre = temporary_genre.split()[-1]
    if temporary_genre:
        bot.send_message(
            message.from_user.id,
            'Чтобы узнать какой фильм подходит вашим требованиям нажми /end',
            reply_markup=keyboard4)


temporary_genre = ''


@bot.message_handler(commands=['end'])
def end(message):
    keyboard5 = telebot.types.ReplyKeyboardMarkup(True)
    keyboard5.row('/continue', '/random_movie')
    flag = True
    bot.send_message(message.from_user.id, 'Подборка для вас:')
    for i in range(0, len(open_file('actor_genres_film.txt'))):
        list_actor_genres_film = open_file('actor_genres_film.txt')[i]
        if temporary_actor in list_actor_genres_film and temporary_genre in list_actor_genres_film:
            flag = False
            piece_list_actor_genres_film = list_actor_genres_film.split(';')
            bot.send_message(message.from_user.id,
                             f'- {piece_list_actor_genres_film[-1]} \n {piece_list_actor_genres_film[-2]}')
    if flag:
        bot.send_message(
            message.from_user.id,
            'Бот не наше фильм по вашим требованиям в своей базе')
    bot.send_message(
        message.from_user.id,
        'Чтобы найти новый фильм нажмите на /continue\nили чтобы получить случайный фильм нажмите /random_movie',
        reply_markup=keyboard5)


bot.polling(none_stop=True, interval=0)