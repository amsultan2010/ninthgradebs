#Abdullah Sultan
#Dr. Sudarsky, Block 6
#2/19/2025, 8:16PM
NICKEL_VAL = 5
DIME_VAL = 10
PENNY_VAL = 1
QUART_VAL = 25
def main():
	numQuarters = 0
	numDimes = 0
	numNickels = 0

	totalMoney = int(input("Enter an amount of money in cents: "))
	if totalMoney > 1:
		print(str(totalMoney) + " cents are: ")
	elif totalMoney == 1:
		print(str(totalMoney) + " cent is: ")
	if totalMoney < 1:
		print("Please enter a value greater than or equal to one.")
	else:
		if totalMoney >= 25:
			numQuarters = totalMoney // QUART_VAL
			totalMoney = totalMoney - (numQuarters * QUART_VAL)
			if numQuarters == 1:
				print(str(numQuarters) + " quarter.")
			else:
				print(str(numQuarters) + " quarters.")
		if totalMoney >=10:
			numDimes = totalMoney // DIME_VAL
			totalMoney = totalMoney - (numDimes * DIME_VAL)
			if numDimes == 1:
				print(str(numDimes) + " dime.")
			else:
				print(str(numDimes) + " dimes.")
		if totalMoney >= 5:
			numNickels = totalMoney // NICKEL_VAL
			totalMoney = totalMoney - (numNickels * NICKEL_VAL)
			if numNickels == 1:
				print(str(numNickels) + " nickel.")
			else:
				print(str(numNickels) + " nickels.")
		if totalMoney > 0:
			if totalMoney == 1:
				print(str(totalMoney) + " penny.")
			else:
				print(str(totalMoney) + " pennies.")
main()
