from turtle import Turtle, Screen

tur = Turtle()
screen = Screen()

def move_forward():
    tur.forward(10)

def move_backward():
    tur.backward(10)

def move_left():
    tur.left(20)

def move_right():
    tur.right(20)

def clear():
    tur.clear()
    tur.penup()
    tur.home()
    tur.pendown()

screen.listen()
screen.onkeypress(key="w" , fun=move_forward)
screen.onkeypress(key="s" , fun=move_backward)
screen.onkeypress(key="a" , fun=move_left)
screen.onkeypress(key="d" , fun=move_right)
screen.onkeypress(key="space" , fun=clear)
screen.exitonclick()
