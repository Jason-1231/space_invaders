from turtle import Turtle, tracer

PACE = 10


class Ship(Turtle):
    def __init__(self):
        self.x = 0
        self.y = -260
        super().__init__()
        self.color('blue')
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.setpos(self.x, self.y)
        self.seth(90)

    def move_left(self):
        if self.xcor() > -210:
            self.x -= PACE
            self.setpos(self.x, self.y)

    def move_right(self):
        if self.xcor() < 200:
            self.x += PACE
            self.setpos(self.x, self.y)


class Bullet(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape('square')
        self.seth(90)
        self.shapesize(0.1, 1)
        self.color('red')
        self.setpos(x, y)




