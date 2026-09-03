#Abdullah Sultan
#Dr. Sudarsky, Block 6
#1/29/2025, 8:58PM
def heightConverter():
	name = str(input("What is your name? "))
	totalHeightCentimeters = int(input("What is your height in centimeters? "))
	totalHeightInches = int((totalHeightCentimeters // 2.54))
	heightFeet = int(totalHeightInches // 12)
	heightInches = int(totalHeightInches % 12)
	print("Hey," + name + "you are " + str(heightFeet) + " feet and " + str(heightInches) + " inches tall.")
heightConverter()
'''
mistakes
constants (12, 2.54) should be defined outside of function and be captial
'''
