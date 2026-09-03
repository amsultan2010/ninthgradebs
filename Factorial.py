#Abdullah Sultan
#Dr. Sudarsky, Block 6
# 2/25/2025, 9:55PM
#This program will calculate the result of an equation with a factorial
def main():
	factorial = 1
	numUser = int(input("Enter a number: "))
	for item in range(1, numUser + 1):
		#assigns factorial the product of all numbers less than/equal to the number itself
		factorial *= item
	print(str(numUser) + "! = " + str(factorial) + ".")
main()
