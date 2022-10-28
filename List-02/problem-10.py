""" 
Write a Python class named Distance constructed by two points (x1, y1), (x2, y2) and a method which will compute the distance between those points.

"""


class Distance:
    def __init__(self):
        self.x1 = int(input("Enter x1: "))
        self.y1 = int(input("Enter y1: "))
        self.x2 = int(input("Enter x2: "))
        self.y2 = int(input("Enter y2: "))

    def distance(self):
        return ((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2) ** 0.5


d = Distance()
dis_val = d.distance()

print(f"Distance is: {dis_val}")
