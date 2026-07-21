from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt", "r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0,270)
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def display_game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", align=ALIGNMENT, font=FONT)
        self.goto(0, -50)
        self.write(arg="Press 'space' to start", align=ALIGNMENT, font=FONT)
