from turtle import Turtle

class Decoration(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.draw_t_line()
        self.draw_b_line()

    def draw_t_line(self):
        self.penup()
        self.goto(-380, 290)
        self.pendown()
        self.goto(380, 290)

    def draw_b_line(self):
        self.penup()
        self.goto(-380, -290)
        self.pendown()
        self.goto(380, -290)
        self.hideturtle()
