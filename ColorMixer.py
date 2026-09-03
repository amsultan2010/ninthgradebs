#Abdullah Sultan
#Dr. Sudarsky, Block 6
#2/12/2025, 2:37PM
def main():
	firstPrimColor = input("Enter your first primary color. ")
	secondPrimColor = input("Enter your second primary color. ")
	#formats the variable to lowercase in the case that the user entered it with varying capitalization i.e. yEllow or YelloW
	firstPrimColor = firstPrimColor.lower()
	secondPrimColor = secondPrimColor.lower()
	if firstPrimColor == "red" and secondPrimColor == "blue" or firstPrimColor == "blue" and secondPrimColor == "red":
		finalMixedColor = "purple"
		print("Mixing " + firstPrimColor + " and " + secondPrimColor + " makes " + finalMixedColor + ".")
	#Makes sure that the final color is the same no matter what the order of the two primaries is
	elif firstPrimColor == "red" and secondPrimColor == "yellow" or firstPrimColor == "yellow" and secondPrimColor == "red":
		finalMixedColor = "orange"
		print("Mixing " + firstPrimColor + " and " + secondPrimColor + " makes " + finalMixedColor + ".")
	#Makes sure that the final color is the same no matter what the order of the two primaries is
	elif firstPrimColor == "blue" and secondPrimColor == "yellow" or firstPrimColor == "yellow" and secondPrimColor == "blue":
		finalMixedColor = "green"
		print("Mixing " + firstPrimColor + " and " + secondPrimColor + " makes " + finalMixedColor + ".")
	#Makes sure that the final color is the same no matter what the order of the two primaries is
	elif firstPrimColor == secondPrimColor:
		finalMixedColor = firstPrimColor
		print("Mixing " + firstPrimColor + " and " + secondPrimColor + " makes " + finalMixedColor + ".")
main()
