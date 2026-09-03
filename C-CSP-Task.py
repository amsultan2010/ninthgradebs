#This library is used to create a table and was installed using pip install in a virtual environment in Visual Studio Code
from tabulate import tabulate

TOTAL_RACES = 24

#List of all drivers (including reserve)
DRIVER_LIST = [
    
    "Lando Norris", "Oscar Piastri",
    
    "Charles Leclerc", "Carlos Sainz",
    
    "Max Verstappen", "Sergio Perez", 
    
    "Lewis Hamilton", "George Russell",
    
    "Fernando Alonso", "Lance Stroll", 
     
    "Pierre Gasly", "Esteban Ocon", "Jack Doohan", 
    
    "Nico Hulkenberg", "Kevin Magnussen", "Oliver Bearman", 
     
    "Liam Lawson", "Yuki Tsunoda", "Daniel Ricciardo", 
    
    "Alex Albon", "Franco Colapinto", "Logan Sargeant", 
    
    "Valtteri Bottas", "Zhou Guanyu" 
    
]

#List of all teams
TEAM_LIST = [
    
    "McLaren", "McLaren",
    
    "Ferrari", "Ferrari",
    
    "RedBull", "RedBull",
    
    "Mercedes", "Mercedes",
    
    "Aston Martin", "Aston Martin", 
    
    "Alpine", "Alpine", "Alpine",
    
    "Haas", "Haas", "Haas",
     
    "VCARB", "VCARB", "VCARB",
     
    "Williams", "Williams", "Williams",
    
    "Kick Sauber", "Kick Sauber"
    
    
]

#List of all drivers' statistics
RACE_STATS_LIST = [
    
    [374, 13, 4, 2], [292, 10, 2, 4],
    
    [356, 13, 3, 3], [290, 9, 2, 5],
    
    [437, 14, 9, 1], [152, 4, 0, 8],
    
    [223, 5, 2, 7], [245, 4, 2, 6],
    
    [70, 0, 0, 9], [24, 0, 0, 13], 
    
    [42, 1, 0, 10], [23, 1, 0, 14], [0, 0, 0, 24],
    
    [41, 0, 0, 11], [7, 0, 0, 18], [7, 0, 0, 18],
     
    [4, 0, 0, 21], [30, 0, 0, 12], [12, 0, 0, 17], 
     
    [12, 0, 0, 16], [5, 0, 0, 19], [0, 0, 0, 23], 
    
    [0, 0, 0, 22], [4, 0, 0, 20] 
    
]


#Function to calculate the statistics of the drivers and send them to be displayed
def calculateDriverStats(driver1, driver2):
    
    #assigns all the variables to 0
    driver1Points = 0
    driver1Podiums = 0
    driver1Wins = 0
    driver1Standings = 0
    driver1WinPercentage = 0.00
    
    driver2Points = 0
    driver2Podiums = 0
    driver2Wins = 0
    driver2Standings = 0
    driver2WinPercentage = 0.00
    

    #driver index currently not found
    driver1Index = -1
    driver2Index = -1
    
    #assigns the index of the driver to the driver index
    for index in range(len(DRIVER_LIST)):
        if DRIVER_LIST[index] == driver1:
            driver1Index = index
        if DRIVER_LIST[index] == driver2:
            driver2Index = index
    
    #assigns the drivers their stats, calculates win percentage and uses the formula to determine which driver is better
    if driver1Index != -1:
        driver1Points = RACE_STATS_LIST[driver1Index][0]
        driver1Podiums = RACE_STATS_LIST[driver1Index][1]
        driver1Wins = RACE_STATS_LIST[driver1Index][2]
        driver1Standings = RACE_STATS_LIST[driver1Index][3]
        driver1MajorStats = ((driver1Wins * 2) + driver1Podiums + (driver1Points / 2)) / (driver1Standings * 0.15)        
        if driver1Wins > 0:
            driver1WinPercentage = f"{round((driver1Wins / TOTAL_RACES) * 100, 2)}%"
        else:
            driver1WinPercentage = "0.00%"
    
    if driver2Index != -1:
        driver2Points = RACE_STATS_LIST[driver2Index][0]
        driver2Podiums = RACE_STATS_LIST[driver2Index][1]
        driver2Wins = RACE_STATS_LIST[driver2Index][2]
        driver2Standings = RACE_STATS_LIST[driver2Index][3]
        driver2MajorStats = ((driver2Wins * 2) + driver2Podiums + (driver2Points / 2)) / (driver2Standings * 0.15)
        
        if driver2Wins > 0:
            driver2WinPercentage = f"{round((driver2Wins / TOTAL_RACES) * 100, 2)}%"
        else:
            driver2WinPercentage = "0.00%"
    
    if driver1MajorStats == driver2MajorStats:
        betterDriver = "both"
    
    else:
        betterDriver = driver1 if driver1MajorStats > driver2MajorStats else driver2
    
    
    #displays driver stats if both had the same number
    if driver1Wins == driver2Wins:
        moreWins = "both" + "(" + str(driver1Wins) + ")"
    
    else:
        moreWins = driver1 if driver1Wins > driver2Wins else driver2
    
    
    if driver1Podiums == driver2Podiums:
        morePodiums = "both" + "(" + str(driver1Podiums) + ")"
    
    else:
        morePodiums = driver1 if driver1Podiums > driver2Podiums else driver2
    
    
    if driver1Points == driver2Podiums:
        morePoints = "both" + "(" + str(driver1Points) + ")"
    
    else:
        morePoints = driver1 if driver1Points > driver2Points else driver2

    
    #sends the stats to be displayed
    return driver1Points, driver1Podiums, driver1Wins, driver1Standings, driver1WinPercentage, driver2Points, driver2Podiums, driver2Wins, driver2Standings, driver2WinPercentage, betterDriver, moreWins, morePodiums, morePoints


#function to display all stats
def showDriverStats(driver1, driver2):
    
    if (driver1 in DRIVER_LIST) and (driver2 in DRIVER_LIST):

        if driver1 == driver2:
            print("You entered the same driver twice. Please enter two different drivers.")
        
        else:
            print("\nHere are two graphs that array the statistics of the drivers selected: ")
            stats = calculateDriverStats(driver1, driver2)
            
            driver1Points, driver1Podiums, driver1Wins, driver1Standings, driver1WinPercentage, driver2Points, driver2Podiums, driver2Wins, driver2Standings, driver2WinPercentage, betterDriver, moreWins, morePodiums, morePoints = stats
            
            if betterDriver == "both":
                print(f"According to the program's algorithm, both of the drivers you selected had roughly equal seasons, since they both performed similarly.")
            else:
                print(f"According to the program's algorithm, \x1B[3m{betterDriver}\x1B[0m performed more and had a better season overall.")

            #prints the table headers in italics
            tableHeaders = ["Statistics", "\x1B[3m" + driver1 + "\x1B[0m", "\x1B[3m" + driver2 + "\x1B[0m"]
            tableData = [
                ["Total Points", driver1Points, driver2Points],
                ["Final Standings", driver1Standings, driver2Standings],
                ["Total Podiums", driver1Podiums, driver2Podiums],
                ["Total Wins", driver1Wins, driver2Wins],
                ["Win Percentage", driver1WinPercentage, driver2WinPercentage]
            ]
            print("Overall Statistics of Both Drivers: ")
            print(tabulate(tableData, headers=tableHeaders, tablefmt="grid"))

            secondTableHeaders = "Statistics Category", "Driver with More"
            secondTableData = [
                ["Driver with More Points", "\x1B[3m" + morePoints + "\x1B[0m"],
                ["Driver with More Podiums", "\x1B[3m" + morePodiums + "\x1B[0m"],
                ["Driver with More Wins", "\x1B[3m" + moreWins + "\x1B[0m"]
            ]

            print("\nDriver with More Points, Podiums, and Wins: ")
            print(tabulate(secondTableData, headers=secondTableHeaders, tablefmt="grid"))
    
    elif driver1 != "Stop" and driver2 != "Stop":
        print("Please enter a valid driver name. You may have made a spelling error.")


def main():
    
    driver1 = ""
    driver2 = ""
    
    print("Welcome to the 2024 Formula One Driver Statistics and Comparison Program!")
    print("This program provides statistics and performance comparisons between two drivers from the 2024 Formula One Season. You can view a chart that directly compares both drivers, and the program will tell you, based on its own algorithm, which driver it thinks had a better season.")
    print(f"\nHere are the drivers you can enter:")
    
    for driver in range(0, len(DRIVER_LIST)):
        print(DRIVER_LIST[driver])
    
    while driver1 != "Stop" and driver2 != "Stop":
        #asks the user for drivers
        driver1 = input("\nEnter a driver from the 2024 Formula One Season, or say 'Stop' to quit the program: ").title()
        
        if driver1 == "Stop":
            break
            
        driver2 = input("Enter another driver from the 2024 Formula One Season, or say 'Stop' to quit the program: ").title()
        
        if driver2 == "Stop":
            break

        #displays driver stats
        showDriverStats(driver1, driver2)
    
    #ends the program
    print("\nProgram terminated. Thanks for using.")


main()