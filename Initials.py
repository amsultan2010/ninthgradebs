# Abdullah Sultan
# Dr. Sudarsky, Block 6
# 3/4/25, 10:10AM
# This program tells the user their initials based on their full name
def main():
    name = input("Enter your full name (first middle last): ")
    # Remove leading and trailing spaces manually
    start = 0
    end = len(name) - 1
    while start <= end and name[start] == ' ':
        start += 1
    while end >= start and name[end] == ' ':
        end -= 1
    name = name[start:end+1]
    # Check if the name is not empty
    if not name:
        print("You didn't enter a name!")
        return
    # Initialize initials
    initials = ""
    # Add the first character of the name as the first initial
    initials += name[0].upper() + "."
    # Loop through the name to find spaces and add the next character as an initial
    for i in range(1, len(name)):
        if name[i - 1] == ' ' and name[i] != ' ':
            initials += name[i].upper() + "."
    print("Your initials are " + initials)
main()