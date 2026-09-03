#Abdullah Sultan
#Dr. Sudarsky, Block 6
#5/7/2025, 8:01PM
#I have neither given nor recieved any unauthorized aid on this prog-ex
#This program, if the user enters a file that is in the same floder as the program, it will print the last 5 lines.

# import os module for file eixstence check
import os

def main():
    # ask user for file name
    filename = input("What file do you want to see? ")
    
    # check if file exists
    if not os.path.isfile(filename):
        print("ERROR: The file " + filename + " doesn't exist.")
        return
    
    # if file exists, display last 5 lines
    display_file_foot(filename)

def display_file_foot(filename):
    # open file in read mode
    file = open(filename, "r")
    
    # read all lines
    lines = file.readlines()
    
    # close the file
    file.close()
    
    # remove newline characters and get last 5 lines
    lines = [line.rstrip('\n') for line in lines]
    last_lines = lines[-5:] if len(lines) >= 5 else lines
    
    # display results
    print("The last " + str(len(last_lines)) + " lines of the file are:")
    for line in last_lines:
        print(line)

# call main function
main()