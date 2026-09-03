#Abdullah Sultan
#Dr. Sudarsky, Block 6
#1/28/2025, 3:52PM

def tempConverter():
	tempCelsius = int(input("Enter the temperature in celsius: "))
	(tempFahrehnheit) = (tempCelsius * (9/5)) + 32
	tempFahrehnheit = int(tempFahrehnheit)
	print("The temperature in Fahrehnheit is " + str(tempFahrehnheit) + " degrees.")
tempConverter()