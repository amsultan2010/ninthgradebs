#Abdullah Sultan
#Dr. Sudarsky, Block 6
#2/7/25, 9:19AM
#This program will convert a percentage to a letter grade
def main():
	gradePercentage = float(input("Enter your grade: "))
	if gradePercentage >= 90.0 and gradePercentage <= 100.0:
		print("Your letter grade: A")
	elif gradePercentage >= 80.0 and gradePercentage < 90.0:
		print("Your letter grade: B")
	elif gradePercentage >= 70.0 and gradePercentage < 80.0:
		print("Your letter grade: C")
	elif gradePercentage >= 60.0 and gradePercentage < 70.0:
		print("Your letter grade: D")
	elif gradePercentage >= 0.0 and gradePercentage < 60.0:
		print("Your letter grade: F")
	else:
		print("Please enter a grade between 0 and 100.")
main()
