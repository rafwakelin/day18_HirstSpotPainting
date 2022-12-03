import turtle
import random

# Select colours from original painting and organize in a list. List has been checked to confirm colours
# therefore code commented out
# import colorgram
# colour_pallet = colorgram.extract('image.jpeg', 30)
# for colour in colour_pallet:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     colours.append(new_colour)

colours = [(235, 228, 211), (104, 106, 125), (213, 152, 91), (186, 62, 32), (225, 212, 109), (230, 176, 172),
           (231, 65, 82), (199, 147, 173), (105, 112, 170), (177, 159, 47), (186, 19, 9), (38, 40, 21), (190, 187, 218),
           (27, 25, 63), (26, 42, 22), (223, 167, 194), (42, 44, 101), (205, 87, 58), (58, 68, 54), (132, 136, 132)]

brush = turtle.Turtle()
brush.shape("circle")
brush.penup()
brush.setposition(-340, -310)
turtle.colormode(255)
brush.speed(0)
brush.shapesize(0.7, 0.7, 1)

def painting_right():
    """Stamps a colour in the canvas traveling on the right direction"""
    for _ in range(14):
        chosen_colour = (random.choice(colours))
        brush.color(chosen_colour)
        brush.stamp()
        brush.forward(50)
    brush.stamp()
    brush.right(90)
    brush.backward(50)
    brush.left(90)


def painting_left():
    """Stamps a colour in the canvas traveling on the left direction"""
    for _ in range(14):
        chosen_colour = (random.choice(colours))
        brush.color(chosen_colour)
        brush.stamp()
        brush.backward(50)
    brush.stamp()
    brush.left(90)
    brush.forward(50)
    brush.right(90)


for _ in range(7):
    painting_right()
    painting_left()

screen = turtle.Screen()
screen.exitonclick()
