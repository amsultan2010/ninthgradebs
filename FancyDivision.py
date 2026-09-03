#Abdullah Sultan
#Dr. Sudarsky, Block 6
#2/4/2025, 8:44PM
def FancyDivision():
	dividend = int(input("Enter a dividend: "))
	divisor = int(input("Enter a divisor: "))
	answer = int(dividend // divisor)
	remainder = int(dividend % divisor)
	if remainder>0:
		print(str(dividend) + " divided by " + str(divisor) + " is " + str(answer) + " with remainder " + str(remainder) + ".")
	else:
		print((str(dividend) + " divided by " + str(divisor) + " is " + str(answer) + "."))
FancyDivision()
