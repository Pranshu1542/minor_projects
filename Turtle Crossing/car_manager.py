from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
Y_POSITION = [-230, -184, -138, -92, -46, 0, 46, 92, 138, 184, 230]
Y_CAR_POSITION = [-207, -115, -23, 69, 161]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
MIN_GAP = 100

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1 or random_chance == 2:
            random_y = random.choice(Y_CAR_POSITION)

            for cars in self.all_cars:
                if cars.ycor() == random_y:
                     if cars.xcor() > 300 - MIN_GAP:
                         return

            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

        remaining_cars = []
        for cars in self.all_cars:
            if cars.xcor() > -400:
                remaining_cars.append(cars)
        self.all_cars = remaining_cars

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def create_line(self):
        self.hideturtle()
        self.penup()

        for y in Y_POSITION:
            self.goto(-400, y)
            self.pendown()
            for _ in range(40):
                self.forward(10)
                self.penup()
                self.forward(10)
                self.pendown()
            self.penup()
