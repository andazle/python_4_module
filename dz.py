from tkinter import *
import random

window = Tk()

w = 600
h = 600

window.geometry('600x600')

# Холст для отрисовки
canvas = Canvas(window, width=w, height=h)
canvas.pack()

# Фон для игры
bg_photo = PhotoImage(file='bg_2.png')


class Knight:
    def __init__(self):
        self.x = 70
        self.y = h // 2
        self.v = 0
        self.v_x = 0
        self.photo = PhotoImage(file='knight.png')

    def up(self, event):
        self.v = -3

    def down(self, event):
        self.v = 3

    def right(self, event):
        self.v_x = +3

    def left(self, event):
        self.v_x = -3

    def stop(self, event):
        self.v = 0


# Класс создания дракона
class Dragon:
    def __init__(self):
        self.x = 750
        self.y = random.randint(100, 500)
        self.v = random.randint(1, 3)
        self.v_x = 0
        self.photo = PhotoImage(file='dragon.png')


knight = Knight()  # Создали рыцаря

# Создает список из трех драконов
dragons = []
for i in range(3):
    dragons.append(Dragon())


def game():
    canvas.delete('all')
    canvas.create_image(h // 2, w // 2, image=bg_photo)
    canvas.create_image(knight.x, knight.y, image=knight.photo)
    knight.y += knight.v
    knight.x += knight.v_x
    canvas.create_image(knight.x, knight.y, image=knight.photo)

    current_dragon = 0
    dragon_to_kill = -1

    for dragon in dragons:
        dragon.x -= dragon.v
        canvas.create_image(dragon.x, dragon.y, image=dragon.photo)

        if ((dragon.x - knight.x) ** 2) + (
                (dragon.y - knight.y) ** 2) <= 96 ** 2:  # 96 - это сумма полуширин дракона и рыцаря
            dragon_to_kill = current_dragon

        current_dragon += 1

        if dragon.x <= 0:
            canvas.delete('all')
            canvas.create_text(300, 300, text='Ты проиграл :(', font='Arial 42', fill='red')
            break

    if dragon_to_kill >= 0:
        del dragons[dragon_to_kill]

    if len(dragons) == 0:
        canvas.delete('all')
        canvas.create_text(300, 300, text='Ты победил!', font='Arial 42', fill='red')
    else:
        window.after(5, game)
        if knight.y <= 52:
            knight.y = 53
        if knight.y >= 544:
            knight.y = 543
        if knight.x <= 50:
            knight.x = 51
        if knight.x >= 550:
            knight.x = 551


game()

window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<Key-Right>', knight.right)
window.bind('<Key-Left>', knight.left)
window.bind('<KeyRelease>', knight.stop)

window.mainloop()