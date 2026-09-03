#Abdullah Sultan
#Dr. Sudarsky, Block 6
#4/8/2025, 5:29PM
#This program tells the user if the letter 'e' appears in the hard-coded srting
def is_letter_e(text):
	return 'e' in text.lower()

def main():
	testStrings = ["I see the letter e.", "How was your day?", "Emily"]
	for string in testStrings:
		if is_letter_e(string):
			print(string + " contains the letter e.")
		else:
			print(string + " does not contain the letter e.")

main()