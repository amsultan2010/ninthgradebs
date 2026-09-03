#Abdullah Sultan
#Dr. Sudarsky, Block 6
#1/31 9:09AM
def IngredientsAdjuster():
	cupsOfSugar = 1.5
	cupsOfButter = 1.0
	cupsOfFlour = 2.75
	numCookies = int(input('How many cookies do you want to make?')) 
	cupsOfSugar = cupsOfSugar * float(numCookies / 48)
	cupsOfButter = cupsOfButter * float(numCookies / 48)
	cupsOfFlour = cupsOfFlour * float(numCookies / 48)
	print("Here are the ingredients you need to make " + str(numCookies) + " cookies:")
	print("You need " + format(cupsOfSugar, '.3f') + " cups of sugar")
	print("You need " + format(cupsOfButter, '.3f') + " cups of butter")
	print("You need " + format(cupsOfFlour, '.3f') + " cups of flour")
IngredientsAdjuster()