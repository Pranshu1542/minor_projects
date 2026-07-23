import turtle
import pandas

screen = turtle.Screen()
screen.title("India State Game")
image = "india_map.gif"
screen.addshape(image)
screen.setup(width=550, height=650)
turtle.shape(image)
screen.tracer(0)

data = pandas.read_csv("indian_states.csv")
all_states = data.state.to_list()

guess = 0
guessed_state = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{guess}/{len(all_states)} States Guessed", prompt="Enter a state")

    if answer_state in all_states and answer_state not in guessed_state:
        guess += 1

        guessed_state.append(answer_state)

        state_data = data[data.state == answer_state]
        new_x_state = float(state_data.x.item())
        new_y_state = float(state_data.y.item())

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(new_x_state, new_y_state)
        t.write(answer_state, align="center", font=("Arial", 8, "normal"))

        if len(guessed_state) == len(all_states):
            game_is_on = False

        screen.update()

turtle.mainloop()