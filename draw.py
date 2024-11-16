'''
Exercise 15.2. Write a function called draw_rect that takes a Turtle object and a Rectangle and uses the Turtle to draw the Rectangle. See Chapter 4 for examples using Turtle objects.

Write a function called draw_circle that takes a Turtle and a Circle and draws the Circle. Solution: https: // thinkpython. com/ code/ draw. py.
'''

import turtle

class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_rect(t, rect):
    """Draw a rectangle using a turtle object.
    t: Turtle
    rect: Rectangle
    """
    t.penup()
    t.goto(rect.corner.x, rect.corner.y)
    t.pendown()
    for length in [rect.width, rect.height, rect.width, rect.height]:
        t.forward(length)
        t.left(90)

bob = turtle.Turtle()
rect = Rectangle(Point(50, 50), 100, 200)
draw_rect(bob, rect)