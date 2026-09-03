#Abdullah Sultan
#Dr. Sudarsky
#3/6/25, 2:09PM
#This program allows the user to guess a number, and  informs them of whether or not their guess is right or not.
import random
def main():
    guess = "incorrect"
    number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")
    while guess == "incorrect":
        numGuess = int(input("Take a guess: "))
        if numGuess < 1 or numGuess > 100:
            print("Please enter a number between 1 and 100.")
        elif numGuess != number:
            guess == "incorrect"
            if numGuess > number:
                print("Too high...")
            else: 
                print("Too low...")
        elif numGuess == number:
            guess = "correct"
            print("Congratulations! You win!")
main()
        