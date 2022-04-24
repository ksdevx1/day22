from turtle import *
import turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.lp_name = "Left Player"
        self.rp_name = "Right Player"
        self.update_scoreboard()
        self.get_names()
        self.update_scoreboard()

    def get_names(self):
        self.lp_name = turtle.textinput("Left Player", "Enter your Name")
        self.rp_name = turtle.textinput("Right Player", "Enter your Name")

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, 290)
        self.write(self.lp_name + " " + str(self.l_score), align="center", font=("Courier", 20, "normal"))
        self.goto(120, 290)
        self.write(str(self.r_score) + " " + self.rp_name, align="center", font=("Courier", 20, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

