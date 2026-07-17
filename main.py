import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Turtle()
turtle.hideturtle()
line = Turtle()
line.hideturtle()
write_score = Turtle()
write_score.hideturtle()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_forward, "w")
screen.onkey(player.move_right, "d")
screen.onkey(player.move_left, "a")

scoreboard.increase_level()
scoreboard.create_coins()

car_manager.create_line()

score = 0
game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    car_manager.create_cars()
    car_manager.move_car()

    for coin in scoreboard.all_coins[:]:
        write_score.penup()
        write_score.goto(280, 250)
        write_score.write(arg=f"Score: {score}", align="right", font=("Courier", 16, "normal"))
        if coin.distance(player) < 10:
            score += 15
            write_score.clear()
            write_score.write(arg=f"Score: {score}", align="right", font=("Courier", 16, "normal"))
            coin.hideturtle()
            scoreboard.all_coins.remove(coin)

    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            turtle.goto(0,250)
            turtle.write(arg=f"Game Over!", align="center", font=("Courier", 24, "bold"))
            break

        if player.ycor() > 300:
            car_manager.increase_speed()
            scoreboard.level += 1
            scoreboard.increase_level()
            scoreboard.create_coins()
            player.goto(0, -280)

screen.exitonclick()