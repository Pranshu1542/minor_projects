from tkinter import *
from tkinter.font import BOLD

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

canvas = Canvas(width=400, height=400, bg=YELLOW)
tomato_img = PhotoImage(file= "tomato.png")
canvas.create_image(200, 200, image=tomato_img)
canvas.create_text(200, 225, text="00:00", fill="white", font=(FONT_NAME, 25, BOLD))
canvas.pack()

label_timer = Label(text= "Timer", font=(FONT_NAME, 40, BOLD), fg=GREEN, bg=YELLOW)
label_timer.place(x=120, y=50)

start = Button(text="Start")
start.place(x=80, y=330)

reset = Button(text="Reset")
reset.place(x=280, y=330)

check = Label(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, BOLD))
check.place(x=180, y=330)

window.mainloop()
