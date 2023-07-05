import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Initialize the player.
player = Player()
# Initialize the cars.
car_manager = CarManager()
# Initialize the scoreboard.
score = Scoreboard()

# Function to catch the pressing of the "Up" key.
screen.onkey(player.go_up, "Up")

game_is_on = True
# While loop that allows us to run the game.
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Call the create car function to create all cars.
    car_manager.create_car()
    # Move all the cars that were created.
    car_manager.move_cars()

    # For loop to verify if the car has crashed against the turtle.
    for car in car_manager.all_cars:
        if player.distance(car) <= 20:
            score.game_over()
            game_is_on = False

    # If statement to verify if player has reached the final position. If yes, restart player position and increase
    # speed and level on the scoreboard.
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.increase_level()

screen.exitonclick()
