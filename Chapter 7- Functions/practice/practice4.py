#Write a Python program that defines a function to calculate the area of a circle, and then
#calls that function with a given radius.
import math
def cal_circle_area(radius):
    area = math.pi * radius**2
    return area
radius = float(input("enter the radius: "))
area_of_circle = cal_circle_area(radius)
print(f"area of circle with radius {radius} is: {area_of_circle}")