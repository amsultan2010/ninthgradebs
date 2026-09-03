#Abdullah Sultan
#Dr. Sudarsky, Block 6
#1/30/2025, 1:01PM
def BoysNGirls():
	numBoys = int(input("How many boys are in the class? "))
	numGirls = int(input("How many girls are in the class? "))
	decBoys = float(numBoys / (numBoys + numGirls))
	decGirls = float(numGirls / (numBoys + numGirls))
	percBoys = int((decBoys * 100) // 1)
	percGirls = int((decGirls * 100) // 1)
	totalKids = str(numBoys + numGirls)
	print("The class has " + totalKids + " students. The class is ", percBoys,"% boys and ", percGirls,"% girls.")
BoysNGirls()