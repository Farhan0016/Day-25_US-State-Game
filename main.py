# TODO 1: Convert the guess to Title case
# TODO 2: Check if the guess is among the 50 states
# TODO 3: Write correct guesses onto the map
# TODO 4: Use a loop to allow the user to keep guessing
# TODO 5: Record the correct guesses in a list
# TODO 6: Keep track of the score

import pandas
import turtle

screen = turtle.Screen()
screen.title(titlestring="U.S. State Game ")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_state)}/50 Guess the states",
                                    prompt="What's another state name?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_state:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer_state in all_states:
        guessed_state.append(answer_state)
        timmy = turtle.Turtle()
        timmy.hideturtle()
        timmy.penup()
        state_data = data[data["state"] == answer_state]
        timmy.goto(int(state_data.x.item()), int(state_data.y.item()))
        timmy.write(answer_state)
        # timmy.write(state_data.state.item())