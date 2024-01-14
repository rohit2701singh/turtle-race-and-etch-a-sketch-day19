from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def w_key():
    tim.forward(20)

def s_key():
    tim.backward(20)

def a_key():
    tim.left(10)

def d_key():
    tim.right(10)

def c_key():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(w_key, "w")
screen.onkey(s_key, "s")
screen.onkey(a_key, "a")
screen.onkey(d_key, "d")
screen.onkey(c_key, "c")

screen.exitonclick()
