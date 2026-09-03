#Abdullah Sultan
#Programming 6 - Quiz 1
#This tells you how long it takes to cook a turkey based on its weight
COOK_TIME_PER_POUND = 20 #this is how long it takes to cook a turkey per pound
MIN_PER_HOUR = 60 #this is how many minutes there are in an hour
def main():
	userName = input("What is your name? ") #asks for the user's name
	lbsTurkeyWeight = float(input("How much does the turkey weigh (in pounds)? ")) #asks for the turkey's weight
	minToCook = lbsTurkeyWeight * COOK_TIME_PER_POUND #this finds out how many minutes are needed to cook
	hoursToCook = int(minToCook // MIN_PER_HOUR) #this finds out how many hours are used to cook
	remainderMinToCook = int(minToCook % MIN_PER_HOUR) #this finds out how many minutes remain after finding out the number of hours required to cook
	print("Hey, " + userName + ", your turkey needs " + str(hoursToCook) + " hours and " + str(remainderMinToCook) + " minutes to cook.")  #greets user, tells them how long it will take for the turkey to cook 
main()
