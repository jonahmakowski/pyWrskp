import turtle
import time


class Turtle:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)

    def draw_grid(self):
        def draw(t, length):
            t.pd()
            t.forward(length)
            t.left(90)
            t.pu()
            t.forward(25)
            t.left(90)
            t.forward(length)
            t.right(180)
        self.t.penup()
        self.t.goto(-500, 420)
        self.t.right(90)

        for i in range(35):
            draw(self.t, 800)

        self.t.right(90)

        for i in range(33):
            draw(self.t, 900)
        time.sleep(5)

    def draw_shape(self):
        sides = int(input('How many sides?'))
        length = int(input('How long?'))
        corner = 360 / sides

        self.t.pu()
        self.t.goto(-400, 400)
        self.t.pd()

        for i in range(sides):
            self.t.forward(length)
            self.t.right(corner)
        time.sleep(5)


tit = Turtle()
tit.draw_shape()
