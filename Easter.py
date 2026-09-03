#Abdullah Sultan
#Unit 2 Programming Quiz 10 pts
#Dr. Sudarsky, Block 6
#2/20/2025, 10:29AM
MARCH_DATE = 22
DAYS_IN_MARCH = 31
MIN_YEAR = 1982
MAX_YEAR = 2048
PRESENT_YEAR = 2025
def main():
	y = int(input("What year do you want to process? "))
	if y >= PRESENT_YEAR:
		timeOfEaster = "future"
	else:
		timeOfEaster = "past"
	if y < MIN_YEAR or y > MAX_YEAR:
		print("The year must be between 1982 and 2048 inclusive.")
	else:
		a = y % 19
		b = y % 4
		c = y % 7
		d = ((19 * a) + 24) % 30
		e = ((2 * b) + (4 * c) + (6 * d) + 5) % 7
		totalDate = MARCH_DATE + d + e
		if totalDate <= DAYS_IN_MARCH:
			monthEaster = "March" 
		else: 
			monthEaster = "April"
			totalDate -= DAYS_IN_MARCH
		if timeOfEaster == "future":
			print("In " + str(y) + ", Easter will be on " + str(monthEaster) + " " + str(totalDate) + ".")
		else:
			print("In " + str(y) + ", Easter was on " + str(monthEaster) + " " + str(totalDate) + ".")
main()
