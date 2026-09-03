#Abdullah Sultan
#Dr. Sudarsky, Block 6
#2/26/2025, 6:09PM
#This program  calculates the money earned if the number of pennies doubles.
def main():
	days = int(input("How many days do you want to look at? "))
	if days < 1:
		print("Please enter a value greater than or equal to 1.")
	else: 
		daily_pay = 1  # in pennies
		total_pay = 0  # in pennies

		print("Daily Pay")
		print("--------------")

		for day in range(1, days + 1):
			print(" " + str(day) + "       " + str(daily_pay))
			total_pay += daily_pay
			daily_pay *= 2

		total_pay_dollars = total_pay / 100
		print("\nYour total pay over the " + str(days) + " days is $" + str(round(total_pay_dollars, 2)) + ".")

main()