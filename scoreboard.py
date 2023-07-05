from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    # Initialize the scoreboard and define the characteristics.
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=260)
        self.write_score()

    # Method that allows us to increase the level that will be written on the score board and write the scoreboard.
    def increase_level(self):
        self.clear()
        self.level += 1
        self.write_score()

    # Method that writes the scoreboard.
    def write_score(self):
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    # Method that writes "Game Over" if the car crashes against the turtle.
    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over", align="center", font=FONT)
