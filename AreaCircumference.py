#Abdullah Sultan
#Dr. Sudarsky, Block 6
#I have neither given nor received any unauthorized aid on this prog-ex. 
#This program calculates the area and circumference based on the radius of a circle
#math library that contains pi
import math

#function that calculates area of the circle
def circle_area(radius):
	return math.pi * radius ** 2

#function that calculates circumference of the circle
def circle_circumference(radius):
	return 2 * math.pi * radius

#main function
def main():
	radius = float(input("Enter the radius of the circle: "))
	area = circle_area(radius)
	circumference = circle_circumference(radius)
	print(f"Area: {area:.4f}")
	print(f"Circumference: {circumference:.4f}")
main()