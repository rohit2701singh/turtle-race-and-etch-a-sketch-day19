from turtle import Turtle, Screen

tim = Turtle()


def movement():
    tim.forward(30)
    tim.left(30)
    # tim.forward(30)


screen = Screen()
screen.listen()
screen.onkey(movement, "space")

screen.exitonclick()
