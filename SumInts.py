#Abdullah Sultan
#Dr. Sudarsky, Block 6
#4/8/2025, 8:01PM
#This porgram takes a positive integer and returns the sum of the integers that are less than the number.
#I have neither given nor received any unauthorized aid on this prog-ex

def sum_ints(number):
    return sum(range(number))

def main():
	testNumbers = [5, 25, 10]
	expectedResults = [10, 300, 45]
	for num, expected in zip(testNumbers, expectedResults):
		result = sum_ints(num)
		print("Number: " + str(num))
		print("Expected: " + str(expected))
		print("Found: " + str(result))
		if result != expected:
			print("--> Error")

main()