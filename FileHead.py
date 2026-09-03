#Abdullah Sultan
#Dr. Sudarsky, Block 6
#5/7/2025, 7:52PM
#I have neither given nor received any unauthorized aid on this prog-ex
#This program, if the user enters a file that is in the same folder as the program, it will print the first 5 lines.
# import os module for file existence check
import os

def main():
    # ask user for file name
    filename = input("What file do you want to see? ")
    
    # check if file exists
    if not os.path.isfile(filename):
        print("ERROR: The file " + filename + " doesn't exist.")
        return
    
    # if file exists, display first 5 lines
    display_file_head(filename)

def display_file_head(filename):
    # open file in read mode
    file = open(filename, "r")
    
    # read first 5 lines
    lines = []
    for i in range(5):
        line = file.readline()
        if line == "":  # end of file reached
            break
        line = line.rstrip("\n")  # remove newline character
        lines.append(line)
    
    # close the file
    file.close()
    
    # display results
    print("The first " + str(len(lines)) + " lines of the file are:")
    for line in lines:
        print(line)

# call main function
main()