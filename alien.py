from turtle import Turtle
PACE = 6
DOWN_PACE = 9


class Alien(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        # self.shapesize(stretch_wid=2, stretch_len=2)
        self.color('red')
        self.penup()
        self.seth(270)
        self.num = None

    def destroy(self):
        self.hideturtle()
        self.setpos(0, 400)

    def move_right(self):
        new_x = self.xcor() + PACE
        self.setpos(new_x, self.ycor())

    def move_left(self):
        new_x = self.xcor() - PACE
        self.setpos(new_x, self.ycor())

    def move_down(self):
        new_y = self.ycor() - DOWN_PACE
        self.setpos(self.xcor(), new_y)

