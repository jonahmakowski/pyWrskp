import turtle
import time

class Turtle:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(9)
    def draw_grid(self):
        def draw(t):
            t.pd()
            t.forward(800)
            t.left(90)
            t.pu()
            t.forward(25)
            t.left(90)
            t.forward(800)
            t.right(180)
        self.t.penup()
        self.t.goto(-500, 420)
        self.t.right(90)
        for i in range(35):
            draw(self.t)

tit = Turtle()
tit.draw_grid()
