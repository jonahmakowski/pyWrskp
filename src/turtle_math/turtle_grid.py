import turtle


class Grid:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.draw_grid()
        self.found_cors = []

    def draw_grid(self):
        self.t.penup()
        self.t.goto(-400, 0)
        self.t.pendown()

        for t in range(20):
            self.t.forward(20)
            self.t.right(90)
            self.t.penup()
            self.t.forward(10)
            self.t.write(t + 1)
            self.t.backward(10)
            self.t.left(90)
            self.t.pendown()

        for i in range(19):
            self.t.left(90)
            self.t.penup()
            self.t.forward(20)
            self.t.left(90)
            self.t.pendown()
            self.t.forward(400)
            self.t.penup()
            self.t.backward(400)
            self.t.right(180)

        xcor = self.t.xcor()
        ycor = self.t.ycor()
        self.t.right(90)

        self.t.backward(20)

        for t in range(20):
            self.t.forward(20)
            self.t.right(90)
            self.t.penup()
            self.t.forward(10)
            self.t.write(20 - t)
            self.t.backward(10)
            self.t.left(90)
            self.t.pendown()

        self.t.goto(xcor, ycor)

        for i in range(20):
            self.t.right(90)
            self.t.forward(20)
            self.t.left(90)
            self.t.forward(380)
            self.t.backward(380)

    def find_cor(self, xcor, ycor):
        if xcor > 20 or ycor > 20:
            print('number too high')
            return
        elif xcor < 0 or ycor < 0:
            print('number too low')
            return
        xcor = xcor * 20 - 400
        ycor = ycor * 20
        self.t.shape('circle')
        self.t.penup()
        self.t.goto(xcor, ycor)
        self.t.stamp()
        self.found_cors.append([xcor, ycor])

    def draw(self):
        if len(self.found_cors) > 2:
            self.t.penup()
            xcor = self.found_cors[0][0]
            ycor = self.found_cors[0][1]
            self.t.goto(xcor, ycor)
            self.t.pendown()
            del self.found_cors[0]

            for item in self.found_cors:
                temp_xcor = item[0]
                temp_ycor = item[1]
                self.t.goto(temp_xcor, temp_ycor)

            self.t.goto(xcor, ycor)
            for item in self.found_cors:
                del item


C = Grid()
C.find_cor(4, 10)
C.find_cor(10, 4)
C.find_cor(1, 4)
C.draw()
input()
