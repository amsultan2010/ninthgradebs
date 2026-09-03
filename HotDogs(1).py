#Abdullah Sultan
#5/1/2025, 8:48AM
#Dr. Sudarsky, Block 6
#I have neither given nor received any unauthorized aid on this programming quiz.
#This program calculates the number of packages of hot dogs and the number of packages of buns needed for a cookout.

def main():
    # get user input for number of people and hot dogs per person
    numPeople = int(input("How many people are coming to the cookout? "))
    perPerson = int(input("How many hot dog sandwiches will each person eat? "))
    totalHotDogs = numPeople * perPerson

    # calculate required packages and leftovers for hot dogs and buns
    hdPackages, hdLeftovers = calculate_packages(totalHotDogs, 7)
    bunPackages, bunLeftovers = calculate_packages(totalHotDogs, 8)

    # print the results
    print_info(hdPackages, hdLeftovers, bunPackages, bunLeftovers)

def calculate_packages(required, packageSize):
    # calculate minimum number of packages needed and the leftovers
    packages = (required + packageSize - 1) // packageSize
    leftovers = packages * packageSize - required
    return packages, leftovers

def print_info(hdPkg, hdLeft, bunPkg, bunLeft):
    # display the calculated values in the required format
    #sorry i used f-strings i forgot and couldd only fix one last minute
    print(f"Number of packages of hot dogs: {hdPkg}")
    print(f"Number of hot dogs left over: {hdLeft}")
    print(f"Number of packages of buns: {bunPkg}")
    print("Number of buns left over: " + str(bunLeft))

main()