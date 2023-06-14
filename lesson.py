from tkinter import *

window = Tk()
w = 600
h = 600
window.geometry(str(w) + 'x' + str(h))

canvas = Canvas(window, width=w, height=h, bg='red')
canvas.place(x=0, y=0)


class Knight:

    def __init__(self):
        self.x = 70
        self.y = h // 2
        self.v = 0
        self.photo = PhotoImage(file='OIP.png')


knight = Knight()
canvas.create_image(knight.x, knight.y, image=knight.photo)

window.mainloop()
