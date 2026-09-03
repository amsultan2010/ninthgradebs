#Abdullah Sultan
#Dr. Sudarsky, Block 6
#2/7/225, 11:15PM
DEFAULT_DISCOUNT = 1
DISCOUNT_1 = float(10)
DISCOUNT_2 = float(20)
DISCOUNT_3 = float(30)
DISCOUNT_4 = float(40)
def main():
	quantity = int(input("How many packages do you want to buy? "))
	typicalPrice = quantity * 99
	if quantity < 10 and quantity > 0:
		discount = DEFAULT_DISCOUNT
	if quantity >=10 and quantity <= 19:
		discount = DISCOUNT_1
	elif quantity >=20 and quantity <= 49:
		discount = DISCOUNT_2
	elif quantity >=50 and quantity <= 99:
		discount = DISCOUNT_3
	elif quantity >=100:
		discount = DISCOUNT_4
	else:
		print("Please enter a quantity greater than 0")
		quit()
	discountPrice = typicalPrice * ((100 - discount)/100)
	print("You get a ", discount, "% discount.")
	print("The amount for the purchase is: $" + format(discountPrice, '.2f'))
main()