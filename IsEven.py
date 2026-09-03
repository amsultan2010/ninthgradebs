#Abdullah Sultan
#Dr. Sudarsky, Block 6
#4/8/25, 5:13PM
#This program takes a non-negative number and tells the user if it is true or not using a bool function
#I have neither given nor received any unauthorized aid on this prog-ex
def is_even(number):
	return number % 2 == 0

def main():
	inputNumber = 0
	while inputNumber < 1:
		inputNumber = int(input("Enter a number: "))
		if inputNumber < 1:
			print("The number must be 1 or greater.")
	result = "even" if is_even(inputNumber) else "odd"
	print(str(inputNumber) + " is " + result + ".")

main()