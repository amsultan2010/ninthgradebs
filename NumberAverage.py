#Abdullah Sultan
#Dr. Sudarsky, Block 6
#5/7/2025, 8:08pm
#I have neither given nor received any unauthorized aid on this prog-ex
#This program will calculate the average of all the numbers in a .txt file, ignoring occasionalk strings

# import os module for file existence check
import os

def main():
    # check if file exists
    filename = "numbers.txt"
    if not os.path.isfile(filename):
        print("ERROR: The file " + filename + " doesn't exist.")
        return
    
    # process the file
    total, count = process_numbers_file(filename)
    
    # calculate and display results
    if count > 0:
        average = total / count
        print("There are " + str(count) + " numbers in the file and their average is " + str(round(average, 2)))
    else:
        print("No valid numbers found in the file.")

def is_number(s):
    # check if string can be converted to a number
    s = s.strip()
    if not s:  # empty string
        return False
    
    # check for valid number characters
    allowed_chars = set('0123456789.-')
    has_digit = False
    
    for char in s:
        if char not in allowed_chars:
            return False
        if char.isdigit():
            has_digit = True
    
    # must have at least one digit
    if not has_digit:
        return False
    
    # check for proper decimal format
    if s.count('.') > 1:
        return False
    
    # check for proper negative sign
    if '-' in s and (s.count('-') > 1 or s[0] != '-'):
        return False
    
    return True

def process_numbers_file(filename):
    # initialize counters
    total = 0.0
    count = 0
    
    # open file
    file = open(filename, "r")
    
    # process each line
    for line in file:
        if is_number(line):
            number = float(line.strip())
            total += number
            count += 1
    
    # close file
    file.close()
    
    return total, count

# call main function
main()