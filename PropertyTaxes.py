#Abdullah Sultan
#Dr. Sudarsky, Block 6
#4/8/2025, 8:12PM
#This program calculates the assessment value and property tax or a property
#I have neither given nor received any unauthorized aid on this prog-ex

def property_taxes(propertyValue):
    assessmentValue = propertyValue * 0.60
    propertyTax = (assessmentValue / 100) * 0.72
    return assessmentValue, propertyTax

def main():
    value = float(input("Enter the property value: "))
    assessment, tax = property_taxes(value)
    print("Assessment value: $" + format(assessment, ".2f"))
    print("Property taxes: $" + format(tax, ".2f"))

main()