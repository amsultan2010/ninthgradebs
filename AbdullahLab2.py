#Abdullah Sultan
#Dr. Sudarsky, Block 6
#4/24/25, 5:47PM
#I have neither given nor received any unauthorized aid on this programming lab.
#This program generates an arithmetic quiz for the user that's 10 questions long.

# difficulties: 
# 1. making division questions have clean answers - solved by generating multiples
# 2. handling invalid inputs - solved with a validation function
# 3. tracking score with penalties - solved with careful updates based on input type

import random

def generate_operator():
    # randomly picks one of the four math operators
    return random.choice(['+', '-', '*', '/'])

def generate_operands(operator):
    # creates appropriate operands based on the operator
    if operator != '/':
        # for +, -, *: both operands are 2-9
        return (random.randint(2, 9), random.randint(2, 9))
    else:
        # for division: ensure clean division with no remainder
        divisor = random.randint(2, 9)
        # create a multiple of the divisor between 10 and 99
        multiplier = random.randint(max(2, 10 // divisor), 99 // divisor)
        return (divisor * multiplier, divisor)

def create_question(operand1, operator, operand2):
    # formats the question string
    return str(operand1) + " " + operator + " " + str(operand2) + " = "

def calculate_answer(operand1, operator, operand2):
    # calculates the expected answer
    if operator == '+': return operand1 + operand2
    elif operator == '-': return operand1 - operand2
    elif operator == '*': return operand1 * operand2
    else: return operand1 // operand2

def is_valid_input(userInput):
    # checks if input is 'q' or an integer
    if userInput == 'q': return True
    try:
        int(userInput)
        return True
    except ValueError:
        return False

def process_answer(userInput, expectedAnswer):
    # processes user's answer to determine if correct, skipped, or invalid
    if not is_valid_input(userInput):
        return (False, False, False)
    
    if userInput == 'q':
        return (True, False, True)
    
    userAnswer = int(userInput)
    return (True, userAnswer == expectedAnswer, False)

def play_quiz():
    # runs the actual quiz
    print("Welcome to the Arithmetic Quiz!")
    print("You will be asked 10 questions.")
    print("You can skip a question at any time by entering 'q'.")
    
    score = 0
    questionNum = 1
    
    while questionNum <= 10:
        print("Question", questionNum)
        operator = generate_operator()
        operand1, operand2 = generate_operands(operator)
        question = create_question(operand1, operator, operand2)
        expectedAnswer = calculate_answer(operand1, operator, operand2)
        
        # keep asking until right answer or skip
        asking = True
        while asking:
            userInput = input(question)
            isValid, isCorrect, isSkip = process_answer(userInput, expectedAnswer)
            
            if not isValid:
                print("Please enter an integer or 'q'.")
            elif isSkip:
                asking = False
            elif isCorrect:
                print("Correct!")
                score += 1
                asking = False
            else:
                print("Incorrect, try again!")
                score -= 0.5
            
            print("Current score:", score)
        
        questionNum += 1
    
    print("Final score:", score, "/10")
    print("Bye! Thanks for playing!")

def main():
    # main function that runs the quiz
    play_quiz()
main()