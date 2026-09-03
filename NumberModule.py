#Abdullah Sultan
#Dr. Sudarsky, Block 6
#4/21/2025, 9:58PM
#I have neither given nor received any unauthorized aid on this prog-ex
#This is a module which checks if a number is prime, lists all primes up to a given number, finds all factors of a number, and determines if it's a perfect number.

#math library
import math

#this function makes sure that the input is prime
def is_prime(number):
	if number < 2:
		return False
	for i in range(2, int(math.sqrt(number)) + 1):
		if number % i == 0:
			return False
	return True

#finds the list of prime numbers
def prime_list(n):
	primes = []
	for num in range(2, n + 1):
		if is_prime(num):
			primes.append(num)
	return primes

#sees if the original number can be divided by another number and if so, the other number is a factor
def is_factor(number, factor):
	return number % factor == 0

#this function makes a list of the factors
def factors_list(number):
	factors = []
	for i in range(1, number + 1):
		if is_factor(number, i):
			factors.append(i)
	return factors

#function checks to see if the number is perfect
def is_perfect(number):
	return sum(factors_list(number)) == 2 * number