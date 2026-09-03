#Abdullah Sultan
#Dr. Sudarsky, Block 6
#2/25/2025, 2:02PM
#This program draws a regular polygon based on the number of sides (entered by user)
import turtle
def main():
	numSides = int(input("How many sides do you want the polygon to have? "))
	#draws as many sides as the user requested, incorporates the angle needed to make it a polygon
	if numSides < 3:
		print("Please enter a number of sides greater than or equal to 3")
	else:
		angle = 360 / numSides
		for side in range(1, numSides + 1):
			turtle.right(angle)
			turtle.forward(50)
	turtle.done()
main()