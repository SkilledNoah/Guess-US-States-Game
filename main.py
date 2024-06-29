"""
---------------------------------------
    * Course: 100 Days of Code - Dra. Angela Yu
    * Author: Noah Louvet
    * Day: 25 - Guess US states Game
    * Subject: Pandas Library - csv data
---------------------------------------
"""

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Get coordinates of click on screen
# def get_mouse_click_coord(x,y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coord)
# screen.mainloop()

data = pandas.read_csv("50_states.csv")
guessed_states = []

answer_state = screen.textinput("Guess the State", "Enter the name of a state").title()
all_states = data.state.to_list()
correct_guess = data["state"].eq(answer_state).any()

while len(all_states) > 0:

    if answer_state == "Exit":
        break

    if correct_guess and answer_state in all_states:
        name = turtle.Turtle()
        name.hideturtle()
        # place on map
        state_data = data[data.state == answer_state]
        name.penup()
        name.goto(state_data.x.iloc[0], state_data.y.iloc[0])
        name.write(answer_state)
        all_states.remove(answer_state)

    # Ask question
    answer_state = screen.textinput(f"{50 - len(all_states)}/50 States Guessed", "Enter the name of a state").title()
    correct_guess = data["state"].eq(answer_state).any()


# list comprehension
missing_states = [state for state in all_states]
states_to_learn = pandas.DataFrame(missing_states)
states_to_learn.to_csv("states_not_guessed")

if len(all_states) == 0:
    text = turtle.Turtle()
    text.hideturtle()
    text.write("You've guessed all of the states, congratulations !", align="center", font=("Arial", 20, "bold"))
else:
    name = turtle.Turtle()
    name.hideturtle()
    # place on map
    for state in missing_states:
        state_data = data[data.state == state]
        name.penup()
        name.goto(state_data.x.iloc[0], state_data.y.iloc[0])
        name.color("red")
        name.write(state)
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.goto(0, 250)
    text.write(f"You guessed {50 - len(all_states)} States", align="center", font=("Arial", 20, "bold"))

screen.exitonclick()
