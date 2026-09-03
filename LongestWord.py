#Abdullah Sultan
#Dr. Sudarsky, Block 6
#5/4/2025, 2:31PM
#I have neithr given nor received any unauthroized aid on this prog-ex
#This program finds the longest word in hardcoded paragraph

def main():
    f = open("/home/amsultan/Documents/Documents/Coding/Survey-Intro/Programming/Unit 5/Prog-Ex 3/castles.txt", "r")
    text = f.read()
    f.close()

    longest = ""
    current = ""
    
    for char in text:
        if char.isalpha():
            current += char
        else:
            if len(current) > len(longest):
                longest = current
            current = ""

    if len(current) > len(longest):
        longest = current

    print("The longest word is '" + longest + "' with " + str(len(longest)) + " letters.")

main()