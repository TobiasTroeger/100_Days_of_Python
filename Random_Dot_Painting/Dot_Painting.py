# The program extracts the colors of an image and uses turtle to paint an image of 10 x 10 random colored dots.


import colorgram
import random
import turtle as t


colors_extracted = colorgram.extract("Hirst_painting.jpg", 20)


def random_color(color_list):
    """
    Takes a random color of a color list and transforms the corresponding RGB values into a tuple.
    :param color_list: a list of 20 colors extracted from an image by colorgram
    :return: random RGB color tuple
    """
    chosen_colors = (random.choice(color_list)).rgb
    color_tuple = (chosen_colors[0], chosen_colors[1], chosen_colors[2])
    return color_tuple


def painting_dots(color_list):
    """
    Paints 10 random colored dots from left to right and resets the position of the turtle after completion.
    :param color_list: a list of 20 colors extracted from an image by colorgram
    """
    for i in range(10):
        color = random_color(color_list)
        timmy.dot(10, color)
        timmy.forward(50)
    timmy.setposition(-250, -250 + y)


timmy = t.Turtle()
timmy.speed(10)
t.colormode(255)
timmy.shape("turtle")
timmy.color("green")
timmy.setposition(-250, -250)
timmy.clear()


y = 50
while y <= 500:
    timmy.penup()
    painting_dots(colors_extracted)
    y += 50

screen = t.Screen()
screen.exitonclick()
