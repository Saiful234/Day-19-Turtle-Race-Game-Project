from turtle import Turtle, Screen
import random
screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_chose = screen.textinput(title="Make your own turtle", prompt="Which turtle will win the race? Enter a color: ")
turtle_color = ["red", "blue", "green", "orange", "purple", "brown"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []


for turtle_index in range(0, 6):
    my_turtle = Turtle(shape="turtle")
    my_turtle.penup()
    my_turtle.color(turtle_color[turtle_index])
    my_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(my_turtle)
if user_chose:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 220:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_chose:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")
        speed_of_turtle = random.randint(1, 10)
        turtle.forward(speed_of_turtle)

screen.exitonclick()