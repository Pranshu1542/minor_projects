from turtle import Turtle
import random

COIN_POSITIONS = [-161, -69, 23, 115, 207]
LEVEL = 1
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = LEVEL
        self.all_coins = []
        self.hideturtle()
        self.penup()
        self.goto(-280,250)

    def increase_level(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def create_coins(self):
        for coin in self.all_coins:
            coin.hideturtle()
        self.all_coins = []
        for y in COIN_POSITIONS:
            random_x = random.randint(-280, 280)
            coins = Turtle(shape="circle")
            coins.shapesize(stretch_wid=0.5,stretch_len=0.5)
            coins.color("gold")
            coins.penup()
            coins.goto(random_x, y)
            self.all_coins.append(coins)