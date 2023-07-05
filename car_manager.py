from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        # List of all cars
        self.all_cars = []
        # Define car speed
        self.car_speed = STARTING_MOVE_DISTANCE

    # Method that allows us to create the car.
    def create_car(self):
        # Generate random int to define when a car will be generated to avoid having to many cars.
        random_chance = random.randint(1, 6)
        # Approximately 1 in 6 times a car will be generated.
        if random_chance == 1:
            # Define all characteristics of the car.
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            # Generate the car randomly on a Y coordinate.
            random_y = random.randint(-250, 250)
            # Put the car on the defined coordinates.
            new_car.goto(x=300, y=random_y)
            # Append the created car to the list.
            self.all_cars.append(new_car)

    # Method that allows us to move the car by the defined speed.
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    # Method that allows us to increase the speed of teh car once the turtle reaches the final position.
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
