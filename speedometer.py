from turtle import Turtle

class Speedometer(Turtle):

    def __init__(self, sleep_time):
        super().__init__()
        self.ball_speed = 10/sleep_time
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_speedometer()

    def update_speedometer(self):
        self.clear()
        self.goto(200, -345)
        self.write( "Speed: " + str(round(self.ball_speed, 1)), align="center", font=("Courier", 30, "normal"))

    def update_speed(self, sleep_time):
        self.ball_speed = 10/sleep_time
        self.update_speedometer()