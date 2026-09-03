#Abdullah Sultan
#Dr. Sudarsky, Block 6
#2/11/2025, 9:15AM
#This program generates a random integer, asks the user to guess what it is, and then tells them if they are too high, too low, or if they got it.
import random
def main():
	#generates a random integer between 0 and 10
	randomNumber = random.randint(1, 10) 
	print("I'm thinking of a number between 1 and 10.")
	guessedNumber = int(input("Take a guess: "))
	#Determine whether the user guess was too high, too low, right, or invalid
	if guessedNumber > randomNumber and guessedNumber <= 10:
		print("Too high, the number was " + str(randomNumber))
	elif guessedNumber < randomNumber and guessedNumber >= 1:
		print("Too low, the number was " + str(randomNumber)) 
	elif guessedNumber == randomNumber:
		print("That's correct!")
	else: 
		print("Please enter a number between 1 and 10.")
main()