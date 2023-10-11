import turtle
import pandas

screen = turtle.Screen()
screen.screensize(800, 600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
game_is_on = True
was_answer = []


def create(answer, xcor, ycor):
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state.goto(xcor, ycor)
    state.write(f"{answer}", align="center", font=("Arial", 6, "normal"))


while game_is_on:

    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    if answer_state in was_answer:
        print("You already has tried this answer!")

    elif len(was_answer) == len(data.state):
        print("You remember all state")
        game_is_on = False

    elif answer_state in data.state.values:
        was_answer.append(answer_state)
        state_data = data.loc[data.state == answer_state]
        x = int(state_data.x.values)
        y = int(state_data.y.values)
        create(answer_state, x, y)

    else:
        print("This state is not exist")
