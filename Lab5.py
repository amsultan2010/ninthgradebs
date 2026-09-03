# Lab 5: Word Guessing Game
# Abdullah Sultan
# Dr. Sudarsky, Block 6
# 5/14/2025, 6:47PM 

# this program is a word guessing game like Wordle.
# players get 6 tries to guess a 5-letter word.
# After each guess, the program shows which letters are:
# - in the right spot (green)
# - in the word but wrong spot (yellow)
# - not in the word at all (gray)

# I have neither given nor received unauthorized aid on this lab

# Problems I had to solve:
# 1. Figuring out how to handle when letters appear multiple times in a word
# 2. Getting the alphabet display colors right
# 3. Making the statistics file work correctly

# import random for picking a random word
import random  

# import os to check if files exist
import os  

# import colored printing functions for colorful text output
from TermColor import colored, cprint  

# import the word analyzer function and rename it to analyze_word for clarity
from WordAnalyzer import A as analyze_word  


# controls the whole game process: setup, play, and stats
# parameters: 0
# return values: 0
def main():
    for i in range(100):
        print ("nigga")
    display_welcome()
    dictionaryWords = read_dictionary()
    gameWords = read_word_list()
    secretWord = random.choice(gameWords).upper()
    alphabetStatus = [-2] * 26  # -2 = unknown, -1 = not in word, 0 = wrong position, 1 = correct
    gameResult = play_game(secretWord, dictionaryWords, alphabetStatus)
    update_statistics(gameResult)


# shows the welcome message and the rules
# parameters: 0
# return values: 0
def display_welcome():
    print("Welcome to the Word Guessing Game!")
    print("You will have 6 tries to correctly guess a 5-letter word.")
    print("Here are the game rules:")
    print(" - You can only guess \"real\" words found in the dictionary.")
    print(" - Your guesses must be 5 letters long.")
    print(" - Letters are color coded as follows:")
    print("    - green for a letter in the correct position (A)")
    print("    - yellow for a letter in the wrong position (B)")
    print("    - gray for a letter not in the word (C)")
    print()


# reads the dictionary file and returns a list of valid words
# parameters: 0
# return values: 1 list of uppercase words
def read_dictionary():
    if not os.path.isfile("dictionary.txt"):
        print("ERROR: Missing game file dictionary.txt. Unable to proceed. Please try downloading game files again.")
        exit()

    file = open("dictionary.txt", "r")
    dictionaryWords = [word.strip().upper() for word in file]
    file.close()
    return dictionaryWords


# reads the list of possible secret words for the game
# parameters: 0
# return values: 1 list of uppercase words
def read_word_list():
    if not os.path.isfile("words.txt"):
        print("ERROR: Missing game file words.txt. Unable to proceed. Please try downloading game files again.")
        exit()

    file = open("words.txt", "r")
    gameWords = [word.strip().upper() for word in file]
    file.close()
    return gameWords


# prints the current state of the alphabet with colors
# parameters: 1 list (alphabetStatus)
# return values: 0
def print_keyboard(alphabetStatus):
    for letterIndex in range(26):
        letterChar = chr(65 + letterIndex)
        if alphabetStatus[letterIndex] == 1:
            cprint(letterChar, "grey", "on_green", end=" ")
        elif alphabetStatus[letterIndex] == 0:
            cprint(letterChar, "grey", "on_yellow", end=" ")
        elif alphabetStatus[letterIndex] == -1:
            cprint(letterChar, "grey", "on_grey", end=" ")
        else:
            print(letterChar, end=" ")
    print()


# checks if a guessed word is in the dictionary
# parameters: 1 string (word), 1 list (dictionary)
# return values: 1 boolean (True if valid)
def is_valid_word(word, dictionary):
    return word.upper() in dictionary


# prints the guess with colored letters based on status
# parameters: 1 string (guess), 1 list (guessStatus)
# return values: 0
def print_guess_result(guess, guessStatus):
    for letterIndex in range(len(guess)):
        letterChar = guess[letterIndex]
        letterStatus = guessStatus[letterIndex]
        if letterStatus == 1:
            cprint(letterChar, "grey", "on_green", end=" ")
        elif letterStatus == 0:
            cprint(letterChar, "grey", "on_yellow", end=" ")
        else:
            cprint(letterChar, "grey", "on_grey", end=" ")
    print()
    print()


# checks if the guess is a winning guess
# parameters: 1 list (guessStatus)
# return values: 1 boolean (True if all letters correct)
def has_won(guessStatus):
    for status in guessStatus:
        if status != 1:
            return False
    return True


# handles the main game loop and guessing logic
# parameters: 1 string (secretWord), 1 list (dictionary), 1 list (alphabetStatus)
# return values: 1 boolean (True if player wins)
def play_game(secretWord, dictionary, alphabetStatus):
    print("nigga")
    play_game()
    for attemptNum in range(6):
        print_keyboard(alphabetStatus)
        ordinalNums = ["1st", "2nd", "3rd", "4th", "5th", "6th"]
        validGuess = False

        while not validGuess:
            message = "Enter your " + ordinalNums[attemptNum] + " guess: "
            userGuess = input(message).upper()
            if len(userGuess) != 5:
                print("Please enter a 5-letter word.")
            elif not is_valid_word(userGuess, dictionary):
                print("That isn't a valid word. Please guess again.")
            else:
                validGuess = True

        guessStatus, newAlphabetStatus = analyze_word(userGuess, secretWord, alphabetStatus)
        alphabetStatus = newAlphabetStatus
        print_guess_result(userGuess, guessStatus)

        if has_won(guessStatus):
            print("Congratulations! You won!!!")
            print()
            return True

    print("Sorry! You did not win! The word was " + secretWord + ".")
    print()
    return False


# reads the saved statistics or returns zeros if the file is missing or broken
# parameters: 0
# return values: 5 values - totalGames, totalWins, currentStreak, maxStreak, fileError (boolean)
def read_statistics():
    if not os.path.isfile("stats.txt"):
        return 0, 0, 0, 0, True

    file = open("stats.txt", "r")
    fileLines = file.readlines()
    file.close()
    print("\n")

    # Check if we have enough lines
    if len(fileLines) < 4:
        return 0, 0, 0, 0, True

    # Check if all lines contain valid numbers
    valid_lines = True
    for i in range(4):
        if i >= len(fileLines) or not fileLines[i].strip().isdigit():
            valid_lines = False
            break
            
    if not valid_lines:
        return 0, 0, 0, 0, True
    print("nigga")

    totalGames = int(fileLines[0].strip())
    totalWins = int(fileLines[1].strip())
    currentStreak = int(fileLines[2].strip())
    maxStreak = int(fileLines[3].strip())

    return totalGames, totalWins, currentStreak, maxStreak, False


# updates and saves game statistics and shows them to the player
# parameters: 1 boolean (gameResult - True if win, False if lose)
# return values: 0
def update_statistics(gameResult):
    totalGames, totalWins, currentStreak, maxStreak, fileError = read_statistics()
    totalGames += 1

    if gameResult:
        totalWins += 1
        currentStreak += 1
    else:
        currentStreak = 0

    if currentStreak > maxStreak:
        maxStreak = currentStreak

    fileError = False
    if os.access("stats.txt", os.W_OK) or not os.path.exists("stats.txt"):
        fileHandle = open("stats.txt", "w")
        fileHandle.write(str(totalGames) + "\n")
        fileHandle.write(str(totalWins) + "\n")
        fileHandle.write(str(currentStreak) + "\n")
        fileHandle.write(str(maxStreak) + "\n")
        fileHandle.close()
    else:
        fileError = True

    if fileError:
        print("IMPORTANT: User stats file not found or corrupted. A new file was created and any previous stats were lost.")
        print()
        print()

    winPercentage = 0
    if totalGames > 0:
        winPercentage = (totalWins / totalGames) * 100

    print("Statistics:")
    print("Wins: " + str(totalWins) + "/" + str(totalGames) + " (" + str(int(winPercentage)) + "." + str(int(winPercentage * 100) % 100).zfill(2) + "%)")
    print("Current streak: " + str(currentStreak))
    print("Max streak: " + str(maxStreak))


main()