#Abdullah Sultan
#4/16/2025, 10:05PM
#Dr Sudarsky, Block 6
#I have neither given nor received any unauthrozied aid on this prog-ex.
#This program tells the user the number of combinations and permutations of a given set of numbers.
#this function calculates the fact. of the number

def factorial(number):
    factorialResult = 1
    for currentNumber in range(1, number + 1):
        factorialResult *= currentNumber
    return factorialResult

#this function calculates the number of combinations
def choose(totalItems, itemsToChoose):
    if itemsToChoose < 0 or itemsToChoose > totalItems:
        return 0
    return factorial(totalItems) // (factorial(itemsToChoose) * factorial(totalItems - itemsToChoose))

def main():
    #hardcodes test cases
    testCases = [(6, 2), (7, 3), (26, 8)]
    expectedResults = [15, 35, 1562275]
    
    for index in range(len(testCases)):
        totalItems = testCases[index][0]
        itemsToChoose = testCases[index][1]
        combinationResult = choose(totalItems, itemsToChoose)
        expectedValue = expectedResults[index]
        print(str(totalItems) + " choose " + str(itemsToChoose) + " is " + str(combinationResult) + " (expected " + str(expectedValue) + ")")

main()