from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    # Method that allows us to define the turtle and it's characteristics.
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    # Method that allows us to move the turtle forward by the defined distance.
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    # Method that returns True if the turtle has arrived at the finish position that was previously defined.
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    # Method that allows us to restart the turtle position after the final position for a specific level was achieved.
    def go_to_start(self):
        self.goto(STARTING_POSITION)
