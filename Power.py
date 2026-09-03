#Abdullah Sultan
#Dr. Sudarsky, Block 6
#4/8/2025, 7:54PM
#This program takes two non-negative integers and raises one to the power of the other
#I have neither given nor received any unauthorized aid on this prog-ex

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def main():
    testCases = [(5, 2, 25), (4, 4, 256), (3, 10, 59049), (7, 0, 1)]
    for base, exp, expected in testCases:
        calculated = power(base, exp)
        print(str(base) + "^" + str(exp) + " = " + str(calculated) + " (expected " + str(expected) + ")")

main()