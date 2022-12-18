import tkinter as tk
import tkinter.simpledialog as simpledialog
import random
import sys
from decimal import Decimal
from PIL import Image, ImageTk

root = tk.Tk()


canvas = tk.Canvas(root, width=600, height=500, background="#f5c9ef")
canvas.grid(columnspan=3, rowspan=6)

# logo:
logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Instructions
instructions = tk.Label(
    root,
    text="Select Level to Get 10 Questions: ",
    font="Raleway",
    bg="#f5c9ef",
    fg="black",
)
instructions.grid(
    column=1,
    row=1,
)

# Definitions:
def run(x):
    # create a label widget
    my_result_var = tk.StringVar()
    my_ask_var = tk.StringVar()
    my_score_var = tk.StringVar()

    result_label = tk.Label(root, height=1, width=20, textvariable=my_result_var)
    result_label.grid(column=1, row=4)

    ask_label = tk.Label(root, height=1, width=20, textvariable=my_ask_var)
    ask_label.grid(column=1, row=3)

    score_label = tk.Label(root, height=1, width=20, textvariable=my_score_var)
    score_label.grid(column=0, row=3)
    
    score = 0
    level = x
    for i in range(10):
        summand_a = generate_integer(level)
        summand_b = generate_integer(level)
        result = Decimal(summand_a) + Decimal(summand_b)
        for j in range(3):
            try:
                my_ask_var.set(f"{summand_a} + {summand_b} = ?")
                answer = simpledialog.askstring("What is the answer?", "Answer: ", parent = root)
                print(answer, result)
                if answer == None:
                    sys.exit()
            except (ValueError, TypeError):
                pass
            if  Decimal(answer) == result:
                evaluate = "Correct answer!"
                my_result_var.set(evaluate)
                score += 1
                my_score_var.set(score)
                break
            elif j < 2:
                evaluate = "EEE"
                my_result_var.set(evaluate)
                pass
            else:
                evaluate = f"{summand_a} + {summand_b} = {result}"
                my_result_var.set(evaluate)
                break
    my_score_var.set(f'Your Score: {score}')


def generate_integer(level):
    if level == 1:
        return str(random.randint(0, 90) / 10)
    elif level == 2:
        return str(random.randint(0, 900) / 100)
    elif level == 3:
        return str(random.randint(0, 9000) / 1000)


# Level buttons:
level_button1 = tk.Button(
    root,
    text="Level 1",
    command=lambda: run(1),
    font="Raleway",
    bg="white",
    fg="black",
    height=2,
    width=15,
)
level_button1.grid(column=0, row=2)
level_button2 = tk.Button(
    root,
    text="Level 2",
    command=lambda: run(2),
    font="Raleway",
    bg="white",
    fg="black",
    height=2,
    width=15,
)
level_button2.grid(column=1, row=2)
level_button3 = tk.Button(
    root,
    text="Level 3",
    command=lambda: run(3),
    font="Raleway",
    bg="white",
    fg="black",
    height=2,
    width=15,
)
level_button3.grid(column=2, row=2)


root.mainloop()
