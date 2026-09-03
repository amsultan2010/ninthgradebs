#Abdullah Sultan
#Dr. Sudarsky, Block 6
#2/12/2025, 8:50PM
SAUSAGES_PER_PACK = 7
BUNS_PER_PACK = 8

def main():
	numPeople = int(input("How many people are coming to the cookout? "))
	dogsPerPerson = int(input("How many hot dog sandwiches will each person eat? "))
	#adds 1 to SAUSAGES_PER_PACK so it rounds up, not down
	dogsNeeded = numPeople * dogsPerPerson
	if dogsNeeded % SAUSAGES_PER_PACK == 0:
		numSausagePacks = dogsNeeded // SAUSAGES_PER_PACK
		sausagesLeftOver = 0
	else:
		numSausagePacks = (dogsNeeded // SAUSAGES_PER_PACK) + 1
		sausagesLeftOver = (numSausagePacks * SAUSAGES_PER_PACK) - dogsNeeded
	if dogsNeeded % BUNS_PER_PACK == 0:
		numBunPacks = dogsNeeded // BUNS_PER_PACK
		bunsLeftOver = 0
	else:
		numBunPacks = (dogsNeeded // BUNS_PER_PACK) + 1
		bunsLeftOver = (numBunPacks * BUNS_PER_PACK) - dogsNeeded
	#makes sure that the user entered values that make sense
	if numPeople < 1 or dogsPerPerson < 1:
		print("Please enter a values greater than or equal to 1.")
	else:
		print("Number of packages of hotdogs: " + str(numSausagePacks) + ".")
		print("Number of hot dogs left over: " + str(sausagesLeftOver) + ".")
		print("Number of packages of buns: " + str(numBunPacks) + ".")
		print("Number of buns left over: " + str(bunsLeftOver) + ".")
main()
