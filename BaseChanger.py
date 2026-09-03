#Abdullah Sultan
#Dr. Sudarsky, Block 6
#3/6/25, 2:22PM
#This program allows the user to change any number in base 10 to a base in between 1 and 10
def main():
    numberB10 = int(input("Enter a number in base 10: "))
    base = int(input("What base should I convert it to (between 2 and 10)? "))
    digits = []
    original = numberB10
    if original == 0:
        digits.append('0')
    else:
        #this process converts the base 
        while numberB10 > 0:
            remainder = numberB10 % base
            digits.insert(0, str(remainder))
            numberB10 = numberB10 // base
    digitsSTR = ''
    for d in digits:
        digitsSTR += d
    print(str(original) + " in base 10 is equal to " + digitsSTR + " in base " + str(base) + ".")
main()