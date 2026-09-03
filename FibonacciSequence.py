#Abdullah Sultan
#Dr. Sudarsky, Block 6
#2/27/25, 12:24PM
#This program prints out as many numbers of the F.S. as the user requests.
def main():
	n = int(input("How many fibonacci numbers would you like to print (at least 2)? "))
	if n < 2:
		print("Please enter a number greater than or equal to 2. ")
	else:
		fibonacciNumbers = [1, 1]
		for _ in range(2, n):
			nextNumber = fibonacciNumbers[-1] + fibonacciNumbers[-2]
			fibonacciNumbers.append(nextNumber)
		print(fibonacciNumbers)
main()