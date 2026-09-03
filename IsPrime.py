#Abdullah Sultan
#Dr. Sudarsky, Block 6
#2/26/2025, 5:36 PM
#This program determines if an integer is prime or not.
def main():
	firstName = input("Enter your first name: ")
	lastName = input("Enter your last name: ")
	stuID = input("Enter your student ID: ")
	idFirst = ""
	for i in range(3):
		if i < len(firstName):
			idFirst += firstName[i].lower()
	idLast = ""
	for i in range(3):
		if i < len(lastName):
			idLast += lastName[i].lower()
	idNum = ""
	for i in range(3, len(stuID)):
		idNum += stuID[i]
	finalID = idFirst + idLast + idNum
	print("Your system login is: " + finalID)
main()