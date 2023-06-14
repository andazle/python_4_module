from tkinter import *
from random import randint

window = Tk()
window.geometry("600x600")

source = r'C:/Users/genii micli/Desktop/Код будущего модуль 2 2.1/elements'


class Fire:
    image = PhotoImage(file=source + '/fire.png').subsample(4)
    def __add__(self, other):
        if isinstance(other, Water):
            return Aroma

class Water:
    image = PhotoImage(file=source + '/water.png').subsample(4)

    def __add__(self, other):
        if isinstance(other, Earth):
            return Clay
        if isinstance(other, Fire):
            return Aroma


class Wind:
    image = PhotoImage(file=source + '/wind.png').subsample(4)
    def __add__(self, other):
        if isinstance(other, Earth):
            return Dust

class Earth:
    image = PhotoImage(file=source + '/ground.png').subsample(4)

    def __add__(self, other):
        if isinstance(other, Water):
            return Clay
        if isinstance(other, Wind):
            return Dust

class Clay:
    image = PhotoImage(file=source + '/pottery.png').subsample(4)

class Aroma:
    image = PhotoImage(file=source + '/aroma.png').subsample(4)

class Dust:
    image = PhotoImage(file=source + '/dust.png').subsample(4)

canvas = Canvas(window, width=600, height=600)
canvas.pack()

elements = [Fire(), Earth(), Water(), Wind()]

for elem in elements:
    img = canvas.create_image(randint(50, 550), randint(50, 550), image=elem.image)

def move(event):
    image_id = canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)

    if len(image_id) == 2:
        elem_id_1, elem_id_2 = image_id[0], image_id[1]
        element1 = elements[elem_id_1 - 1]
        element2 = elements[elem_id_2 - 1]

        new_element = element2 + element1

        if new_element:
            if new_element not in elements:
                canvas.create_image(event.x, event.y, image=new_element.image)
                elements.append(new_element)


    canvas.coords(image_id, event.x, event.y)

window.bind('<B1-Motion>', move)

window.mainloop()