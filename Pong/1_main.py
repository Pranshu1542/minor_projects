from turtle import Screen, Turtle
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, -50))
l_paddle = Paddle((-350, -50))
ball = Ball()
scoreboard = Scoreboard()

# Dotted-line below scoreboard
line = Turtle()
line.color("white")
line.hideturtle()
line.penup()
line.goto(-400, 200)
line.pendown()
for _ in range(100):
    line.forward(10)
    line.penup()
    line.forward(10)
    line.pendown()
line.penup()

# Display message before starting game
message = Turtle()
message.color("white")
message.hideturtle()
message.penup()
message.goto(0, 20)
message.write(arg="Press 'Space' to start the game", align="center", font=("Courier", 16, "bold"))

game_started = False

def start_game():
    global game_started
    game_started = True
    message.clear()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(start_game , "space")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()

    if not game_started:
        continue

    ball.move()

    #Detect collision with wall
    if ball.ycor() > 190 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 70 and ball.xcor() > 320 or ball.distance(l_paddle) < 70 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    #Detect L paddle misses:
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
