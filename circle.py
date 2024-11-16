'''
Exercise 15.1. Write a definition for a class named Circle with attributes centre and radius, where centre is a Point object and radius is a number. 
Instantiate a Circle object that represents a circle with its centre at (150, 100) and radius 75. Write a function named point_in_circle that takes a Circle and a Point and returns True if the Point lies in or on the boundary of the circle.

Write a function named rect_in_circle that takes a Circle and a Rectangle and returns True if the Rectangle lies entirely in or on the boundary of the circle.

Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns True if any of the corners of the Rectangle fall inside the Circle. Or as a more challenging version, return True if any part of the Rectangle falls inside the Circle.

Solution: https://thinkpython.com/code/Circle.py.
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

class Rectangle:
    def __init__(self, corner, width, height):
        self.corner = corner
        self.width = width
        self.height = height

def point_in_circle(circle, point):
    """Return True if the Point lies in or on the boundary of the circle"""
    return ((point.x - circle.centre.x) ** 2 + 
            (point.y - circle.centre.y) ** 2) <= circle.radius ** 2

def rect_in_circle(circle, rect):
    """Return True if the Rectangle lies entirely in or on the boundary of the circle"""
    # Check all four corners
    corners = [
        Point(rect.corner.x, rect.corner.y),  # bottom-left
        Point(rect.corner.x + rect.width, rect.corner.y),  # bottom-right
        Point(rect.corner.x, rect.corner.y + rect.height),  # top-left
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)  # top-right
    ]
    return all(point_in_circle(circle, corner) for corner in corners)

def rect_circle_overlap(circle, rect):
    """Return True if any of the corners of the Rectangle fall inside the Circle"""
    corners = [
        Point(rect.corner.x, rect.corner.y),  # bottom-left
        Point(rect.corner.x + rect.width, rect.corner.y),  # bottom-right
        Point(rect.corner.x, rect.corner.y + rect.height),  # top-left
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)  # top-right
    ]
    return any(point_in_circle(circle, corner) for corner in corners)

# Create circle with centre at (150, 100) and radius 75
circle = Circle(Point(150, 100), 75)

# Test a point inside the circle
p1 = Point(150, 100)  # centre point
print(point_in_circle(circle, p1))  # Should print True

# Test a rectangle
r1 = Rectangle(Point(140, 90), 20, 20)
print(rect_in_circle(circle, r1))  # Should print True