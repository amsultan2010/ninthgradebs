#Abdullah Sultan
#Dr. Sudarsky, Block 6
#3/5/2025, 8:46AM
#This program removes spaces and reverses the capitalization of the word entered by the user
def main():
	sentence = input("Please, enter a sentence: ")
	result = ""
	for char in sentence:
		if char == " ":
			continue
		if char.isupper():
			result += char.lower()
		elif char.islower():
			result += char.upper()
		else:
			result += char
	print(result)
main()