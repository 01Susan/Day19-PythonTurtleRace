import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=550)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
turtle_all = []
is_race_on = False


def turtles(name, color_code, y_axis):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[color_code])
    new_turtle.penup()
    new_turtle.goto(x=-225, y=y_axis)
    turtle_all.append(new_turtle)


if user_bet:
    is_race_on = True

y = -200
for i in range(0, 6):
    turtles(i, i, y)
    y += 50

while is_race_on:
    for turtle in turtle_all:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
