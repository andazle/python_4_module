from tkinter import *
import time


class Ball():

    def __init__(self, canvas, platform, color):
        self.canvas = canvas # где будет распологаться шарик
        self.platform = platform # для того, чтобы шарик "знал", что можно взаимодействовать с платформой
        self.oval = canvas.create_oval(200, 200, 215, 215, fill=color)
        self.x = 1
        self.y = -2
    

    def draw(self):
        self.canvas.move(self.oval, self.x, self.y)
        position = self.canvas.coords(self.oval) # список из 4 координат шара
        if position[1] <= 0:
            self.y = 2
        if position[3] >= 400: # взаимодествие с низом
            self.touch_platform = True
        if self.touch_platform(position) == True:
            self.y = -2
        if position[0] <= 0:
            self.x = 2
        if position[2] >= 500:
            self.x = -2
    
    def touch_platform(self, ball_pos):
        platform_pos = self.canvas.coords(self.platform.rect)
        if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
            if ball_pos[3] >= platform_pos[1] and ball_pos[1] <= platform_pos[3]:
                return True
        return False


class Platform():

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.rect = canvas.create_rectangle(230, 300, 330, 310, fill=color)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)
    
    def left(self, event):
        self.x = -2

    def right(self, event):
        self.x = 2
    
    def draw(self):
        self.canvas.move(self.rect, self.x, 0)
        position = self.canvas.coords(self.rect) #  координаты платформы
        if position[0] <= 0:
            self.x = 0
        if position[2] >= 500:
            self.x = 0



window = Tk()
window.title('Аркада')
window.resizable(0, 0)

canvas = Canvas(window, width=500, height=400)
canvas.pack()

platform = Platform(canvas, 'blue')
ball = Ball(canvas, platform, 'red')

while True:
    ball.draw()
    platform.draw()
    window.update()
    time.sleep(0.01)