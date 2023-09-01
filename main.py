import turtle
import pandas
import time


"""The Writer"""

writer_turtle = turtle.Turtle()
writer_turtle.hideturtle()
writer_turtle.penup()
writer_turtle.speed(0)

best_score_turtle = turtle.Turtle()
best_score_turtle.hideturtle()
best_score_turtle.penup()


def write(state_name, state_x, state_y):
    writer_turtle.goto(state_x, state_y)
    writer_turtle.write(state_name)


def write_best_score(best_score):
    best_score_turtle.clear()
    best_score_turtle.goto(-200, 220)
    best_score_turtle.write(f"Best Score: {best_score}")


def end():
    writer_turtle.goto(20, -190)
    writer_turtle.write("Congratulations!", move=True, align="left", font=("Arial", 18, "normal"))


"""Start of the Program"""

data = pandas.read_csv("50_states.csv")
guessed_states_list = []
state_count = 0
best_score = 0
try:
    with open("best_score.txt", "r") as best_file:
        best_score = [int(n) for n in best_file.read() if n != ""][0]
except:
    pass

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
screen.title("U.S. States Game")
write_best_score(best_score)

while state_count < 50:
    try:
        user_guess = screen.textinput(f"{state_count}/50 states correct", "Guess the name of a State:").title()
    except:
        break

    if user_guess == "":
        break
    elif user_guess == "Exit":
        break
    else:
        for i in range(0, 50):
            if user_guess == data.at[i, "state"] and user_guess not in guessed_states_list:
                state_name = data.at[i, "state"]
                state_x = data.at[i, "x"]
                state_y = data.at[i, "y"]
                write(state_name, state_x, state_y)
                state_count += 1
                guessed_states_list.append(state_name)
                if state_count > best_score:
                    best_score = state_count
                write_best_score(best_score)
                with open("best_score.txt", "w") as best_file:
                    best_file.write(str(best_score))
                break

if state_count == 50:
    end()
    time.sleep(2)
    raise SystemExit
else:
    states_to_learn_list = []
    for i in range(0, 50):
        if data.at[i, "state"] not in guessed_states_list:
            states_to_learn_list.append(data.at[i, "state"])
            state_name = data.at[i, "state"]
            state_x = data.at[i, "x"]
            state_y = data.at[i, "y"]
            writer_turtle.pencolor("red")
            write(state_name, state_x, state_y)
    states_to_learn_dict = {"States to learn": states_to_learn_list}
    states_to_learn_data = pandas.DataFrame(states_to_learn_dict)
    states_to_learn_data.to_csv("States_to_Learn.csv")
    states_to_learn_data.to_string("States_to_Learn.txt")

screen.exitonclick()
raise SystemExit
