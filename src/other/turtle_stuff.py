import turtle
import time
import random


class Turtle:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)

    def grid(self):
        self.t.pd()
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

    def shape(self):
        self.t.pd()
        sides = int(input('How many sides?'))
        length = int(input('How long?'))
        corner = 360 / sides

        self.t.pu()
        self.t.goto(0, 0)
        self.t.pd()

        for i in range(sides):
            self.t.forward(length)
            self.t.right(corner)
        time.sleep(5)

    def scribble(self):
        self.t.pd()
        self.t.shape('turtle')
        self.t.speed(5)

        blue = turtle.Turtle()
        green = turtle.Turtle()
        yellow = turtle.Turtle()
        pink = turtle.Turtle()
        purple = turtle.Turtle()
        black = turtle.Turtle()

        blue.color('blue')
        green.color('green')
        yellow.color('yellow')
        pink.color('pink')
        purple.color('purple')

        turtles = [blue, green, yellow, pink, purple, yellow, black]

        colors = ['blue', 'green', 'yellow', 'black', 'purple', 'pink']

        while True:
            for item in turtles:
                item.speed(0)

                item.goto(random.randint(-400, 400), random.randint(-400, 400))

                x = item.xcor()
                y = item.ycor()

                self.t.color(colors[random.randint(0, len(colors) - 1)])
                self.t.goto(x, y)


tit = Turtle()
while True:
    do = input('What do you wish to do?\n')
    if do == 'grid':
        tit.grid()
    elif do == 'shape':
        tit.shape()
    elif do == 'scribble':
        tit.scribble()
    else:
        print('That is not an option try again')
