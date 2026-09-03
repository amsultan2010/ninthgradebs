#Abdullah Sultan
#Dr. Sudarsky, Block 6
#5/10/2025, 9:38AM
#I have neitherg iven nor received any unauthorized aid on this lab.

import os


def main():
    print("Welcome to the To-Do List")
    todoList = []
    keepGoing = True
    
    
    # Check if file exists, if not create it
    if not os.path.isfile("todolist.txt"):
        fileObj = open("todolist.txt", "w")
        fileObj.close()
    
    
    # Read contents from existing file
    fileObj = open("todolist.txt", "r")
    todoList = fileObj.read().splitlines()
    fileObj.close()
    
    
    # Print initial list status
    if len(todoList) == 0:
        print("Your to-do list is empty.\n")
    else:
        print_list(todoList)
    
    
    # Main program loop
    while keepGoing:
        choice = get_input()
        
        
        if choice == 1:
            print_list(todoList)
            
        elif choice == 2:
            todoList = mod_list(todoList, "add")
            
        elif choice == 3:
            if len(todoList) == 0:
                print("ERROR: There is nothing in the list. You can't remove any item.")
            else:
                todoList = mod_list(todoList, "remove")
                
        elif choice == 4:
            # Save to file before quitting
            fileObj = open("todolist.txt", "w")
            
            for item in todoList:
                fileObj.write(item + "\n")
                
            fileObj.close()
            print("Bye!")
            keepGoing = False


def print_list(todoList):
    if len(todoList) == 0:
        print("Your to-do list is empty.\n")
        
    else:
        print("Your to-do list contains:")
        
        for i in range(len(todoList)):
            print(str(i+1) + ". " + todoList[i])
            
        print()


def mod_list(todoList, operation):
    if operation == "add":
        newItem = input("Enter the item you would like to add? ")
        
        # Check if item already exists
        for item in todoList:
            if item.lower() == newItem.lower():
                print("ERROR: " + item + " is already in the list.")
                return todoList
                
        todoList.append(newItem)
        print(newItem + " added to the list.\n")
        return todoList
        
    elif operation == "remove":
        removeItem = input("Which item would you like to remove? ")
        
        # Find item
        for item in todoList:
            if item.lower() == removeItem.lower():
                todoList.remove(item)
                print(item + " removed from the list.\n")
                return todoList
                
        print("ERROR: " + removeItem + " is not in the list.")
        return todoList


def get_input():
    while True:
        print("Do you want to:")
        print("1. View your list")
        print("2. Add an item")
        print("3. Remove an item")
        print("4. Quit")
        
        choiceStr = input("Enter your choice: ")
        
        
        if choiceStr.isdigit():
            choice = int(choiceStr)
            
            if choice >= 1 and choice <= 4:
                return choice
        
        
        print("ERROR: This is not an accepted answer.")


main()