from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=500)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle is going to win the race? choose the color: ")
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for turtle in range(0, 6):
    tur = Turtle(shape="turtle")
    tur.penup()
    tur.color(colors[turtle])
    tur.goto(x=-280,y=y_pos[turtle])
    all_turtles.append(tur)

if user_bet:
    is_race_on = True

while is_race_on:
    for move in all_turtles:
        if move.xcor() > 280:
            is_race_on = False
            winning_color = move.pencolor()
            if winning_color == user_bet:
                print(f"You won the race with {winning_color}, Congratulation!")
            else:
                print(f"You lose, the {winning_color} wins the race")

        run = random.randint(0, 10)
        move.forward(run)

screen.exitonclick()
