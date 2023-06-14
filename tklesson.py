from tkinter import *
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

def get_rgb(rgb):
    return "#%02x%02x%02x" % rgb

window = Tk()
window.geometry('400x350')
window.title('Курс валют от банка MAXIMUM')
window['bg'] = get_rgb((255, 102, 24))
window.resizable(width=False, height=False)

img_logo = PhotoImage(file=r'C:\Users\genii micli\Desktop\Код будущего модуль 2 2.1\logo.png')
logo = Label(window, image=img_logo, bg='white')
logo.place(x=0, y=0)

label = Label(window, text='Курс валют \n MAXIMUM банк', fg='white', font='Arial 22', bg=get_rgb((255, 102, 24)))
label.place(x=155, y=30)

data_course = Label(window, text=f'Курс на {today}', font='Arial 18', fg='white', bg=get_rgb((255, 102, 24)))
data_course.place(x=100, y=160)

usd_course = Label(window, text='$:' + get_course('R01235'), font='Arial 16', fg='white', bg=get_rgb((255, 102, 24)))
usd_course.place(x=150, y=200)
eur_course = Label(window, text='€:' + get_course('R01239'), font='Arial 16', fg='white', bg=get_rgb((255, 102, 24)))
eur_course.place(x=150, y=240)
cny_course = Label(window, text='¥:' + get_course('R01375'), font='Arial 16', fg='white', bg=get_rgb((255, 102, 24)))
cny_course.place(x=150, y=280)

window.mainloop()
