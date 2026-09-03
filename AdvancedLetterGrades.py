#Abdullah Sultan
#Dr. Sudarsky, Block 6
#2/7/25, 10:59AM
#This program will convert a percentage to a letter grade
def main():
	gradePercentage = float(input("Enter your grade: "))
	letterGrade = "Not applicable. Please enter a grade between 0.0 and 100.0"
	if gradePercentage >= 90.0 and gradePercentage <= 100.0:
		letterGrade = "A"
		if gradePercentage < 93.0:
			letterGrade = "A-"
		elif gradePercentage < 97.0:
			letterGrade = "A"
		else:
			letterGrade = "A+"
	elif gradePercentage >= 80.0 and gradePercentage < 90.0:
		letterGrade = "B"
		if gradePercentage < 83.0:
			letterGrade = "B-"
		elif gradePercentage < 87.0:
			letterGrade = "B"
		else:
			letterGrade = "B+"
	elif gradePercentage >= 70.0 and gradePercentage < 80.0:
		letterGrade = "C"
		if gradePercentage < 73.0:
			letterGrade = "C-"
		elif gradePercentage < 77.0:
			letterGrade = "C"
		else:
			letterGrade = "C+"
	elif gradePercentage >= 60.0 and gradePercentage < 70.0:
		letterGrade = "D"
		if gradePercentage < 63.0:
			letterGrade = "D-"
		elif gradePercentage < 67.0:
			letterGrade = "D"
		else:
			letterGrade = "D+"
	elif gradePercentage >= 0.0 and gradePercentage < 60.0:
		letterGrade = "F"
	print("Your letter grade: " + letterGrade)
main()
