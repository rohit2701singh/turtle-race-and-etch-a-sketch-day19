from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)

colors = ["red", "brown", "chocolate", "green", "blue", "purple"]
user_bet = screen.textinput("make your bet", f"which tutle will win the race? Enter a color {colors}: ")
y_position = [-150, -100, -50, 0, 50, 100]

all_turtle = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-241, y=y_position[turtle_index])
    # set the x coordinate so that turtle did not disappear from screen.
    all_turtle.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 220:
            # set the xcor value so that turtle did not go out of screen
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you've won. The {winning_color} is the winner.")
            else:
                print(f"you lost. The {winning_color} is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
