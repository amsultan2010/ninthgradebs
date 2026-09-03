#Abdullah Sultan
#Dr. Sudarsky, Block 6
#5/2/2025, 2:02PM
#I have neither given nor received any unauthorized aid on this prog-ex
#This program counts the names in a list


def main():
    num_names = count_names()
    print("There are " + str(num_names) + " names in the file.")

def count_names():
   
    file_path = "/home/amsultan/Documents/Documents/Coding/Survey-Intro/Programming/Unit 5/Prog-Ex 1/names.txt"
    

    f = open(file_path, "r")
    names_list = f.readlines()

    f.close()
    

    return len(names_list)


main()
