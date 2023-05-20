import turtle
import time
from datetime import datetime

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Simple Digit Clock")
screen.setup(width=600, height=400)

# Set up the turtle pen
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)

# Define a function to draw a digit
def draw_digit(x, y, num):
    pen.goto(x, y)
    pen.pendown()
    if num == 0:
        pen.setheading(90)
        pen.forward(50)
        pen.right(90)
        pen.forward(100)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
        pen.forward(100)
    elif num == 1:
        pen.setheading(0)
        pen.forward(50)
        pen.right(135)
        pen.forward(70)
    elif num == 2:
        pen.setheading(90)
        pen.forward(50)
        pen.right(90)
        pen.forward(50)
        pen.right(45)
        pen.forward(70)
        pen.left(135)
        pen.forward(50)
    elif num == 3:
        pen.setheading(90)
        pen.forward(50)
        pen.right(45)
        pen.forward(70)
        pen.left(135)
        pen.forward(50)
        pen.right(135)
        pen.forward(70)
    elif num == 4:
        pen.setheading(180)
        pen.forward(50)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
        pen.forward(50)
        pen.right(135)
        pen.forward(70)
    elif num == 5:
        pen.setheading(90)
        pen.forward(50)
        pen.left(90)
        pen.forward(50)
        pen.left(45)
        pen.forward(70)
        pen.right(135)
        pen.forward(50)
    elif num == 6:
        pen.setheading(90)
        pen.forward(100)
        pen.right(180)
        pen.forward(50)
        pen.right(90)
        pen.forward(50)
        pen.right(45)
        pen.forward(70)
        pen.left(135)
        pen.forward(50)
    elif num == 7:
        pen.setheading(0)
        pen.forward(50)
        pen.right(135)
        pen.forward(70)
        pen.left(45)
        pen.forward(50)
    elif num == 8:
        pen.setheading(90)
        pen.forward(50)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
        pen.forward(100)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
        pen.forward(50)
    elif num == 9:
        pen.setheading(90)
        pen.forward(50)
        pen.right(45)
        pen.forward(70)
        pen.left(135)
        pen.forward(50)
        pen.right(135)
        pen.forward(50)

    pen.penup()

# Define a function to draw the current time
def draw_time():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    # Draw the hours digit
    draw_digit(-220, 0, hour//10)
    draw_digit(-150, 0, hour%10)

    # Draw the minutes digit
    draw
