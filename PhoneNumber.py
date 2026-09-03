#Abdullah Sultan
#Dr. Sudarsky, Block 6
#3/5/2025, 9:11AM
#This program converts a phone number with letters into a phone number with numbers.
TWO = 'ABC'
THREE = 'DEF'
FOUR = 'GHI'
FIVE = 'JKL'
SIX = 'MNO'
SEVEN = 'PQRS'
EIGHT = 'TUV'
NINE = 'WXYZ'

def main():
	phoneNumber = input("Enter a phone number: ")
	valid = True
	for char in phoneNumber:
		if not (char.isalnum() or char == '-'):
			valid = False
	if not valid:
		print(f"The phone number {phoneNumber} is not valid.")
	else:
		numericNumber = ''
		for char in phoneNumber.upper():
			if char in TWO:
				numericNumber += '2'
			elif char in THREE:
				numericNumber += '3'
			elif char in FOUR:
				numericNumber += '4'
			elif char in FIVE:
				numericNumber += '5'
			elif char in SIX:
				numericNumber += '6'
			elif char in SEVEN:
				numericNumber += '7'
			elif char in EIGHT:
				numericNumber += '8'
			elif char in NINE:
				numericNumber += '9'
			else:
				numericNumber += char
		print("The phone number is " + numericNumber + ".")
main()