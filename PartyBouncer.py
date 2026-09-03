#Abdullah Sultan
#Dr. Sudarsky, Block 6
#5/4/2025, 2:13PM
#I have neither given nor received any unauthorized aid on this prog-ex
#This program reads a guest list and sees if it matches user inptu


def remove_newline(text):

    if len(text) > 0 and text[-1] == '\n':  # Check last character
        return text[:-1]  # Return everything except last character
    return text

def main():
    file = open("/home/amsultan/Documents/Documents/Coding/Survey-Intro/Programming/Unit 5/Prog-Ex 2/GuestList.txt", "r")
    guests = []
    for line in file:
        guests.append(remove_newline(line))
    file.close() 

    name = input("What is your name? ")
    name = remove_newline(name)  

    # Check list (basic 'in' operator)
    if name in guests:
        print("You may enter the party. Have fun!")
    else:
        print("Sorry, your name is not on the guest list.")

main()