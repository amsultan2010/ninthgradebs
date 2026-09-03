#Abdullah Sultan
#Dr. Sudarsky, Blokc 6
#3/3/2025, 10:
#This program generates a login ID for the user based on the personal details they enter.
def main():
	firstName = input("Enter your first name: ")
	lastName = input("Enter your last name: ")
	stuID = input("Enter your student ID: ")
	idFirst = firstName[:3]
	idFirst = (idFirst.lower())
	idLast = lastName[:3]
	idLast = (idLast.lower())
	idNum = stuID[3:]
	finalID = idFirst + idLast + idNum
	print("Your system login is: " + finalID)
main()