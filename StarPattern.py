#Abdullah Sultan
#Dr. Sudarsky, Block 6
#2/26/2025, 9:15PM
#This program displays as many star pattern rows as the user requests.
def main():
	numRows = int(input("How many rows of stars do you want to see? "))
	if numRows < 1:
		print("Please enter a value greater than or equal to 1.")
	else:
		for row in range (1, numRows + 1):
			for column in range(1, row + 1):
				print("*", end="")
			print()
main()