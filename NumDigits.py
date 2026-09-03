#Abdullah Sultan
#Dr. Sudarsky, Block 6
#4/8/2025, 10:32PM
#This program takes a positive integer and tellsthe user how many digits it has.
#I have neither given nor received any unauthorized aid on this prog-ex

def num_digits(number):
	count = 0
	while number > 0:
		count += 1
		number = number // 10
	return count

def main():
	testNumbers = [3, 25, 9572]
	for num in testNumbers:
		print("Number of digits in " + str(num) + ": " + str(num_digits(num)))

main()