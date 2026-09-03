#Abdullah Sultan
#Dr. Sudarsky, Block 6
#4/16/2025, 10:12PM
#I have neither given nor received any unauthorized aid on this prog-ex.
#This program uses our old program from unit 2 and makes two functions to tell the user the types of coins required to equal a certain amount of money
NICKEL_VAL = 5
DIME_VAL = 10
PENNY_VAL = 1
QUART_VAL = 25
#this program will take an amount of money in cents and tell the user how many coins of each type are needed to equal that amount
def calculate_coins(total_money):
    num_quarters = total_money // QUART_VAL
    remaining = total_money % QUART_VAL
    
    num_dimes = remaining // DIME_VAL
    remaining %= DIME_VAL
    
    num_nickels = remaining // NICKEL_VAL
    remaining %= NICKEL_VAL
    
    num_pennies = remaining
    
    return num_quarters, num_dimes, num_nickels, num_pennies
#this function will take the number of coins and the type of coin and print out the number of coins needed
def print_coins(count, coin_type):
    if count > 0:
        if count == 1:
            print(str(count) + " " + coin_type + ".")
        else:
            if coin_type == "penny":
                print(str(count) + " pennies.")
            else:
                print(str(count) + " " + coin_type + "s.")
#this function will take the total amount of money and call the other two functions to calculate the number of coins needed and print them out
def main():
    total_money = int(input("Enter an amount of money in cents: "))
    
    if total_money > 1:
        print(str(total_money) + " cents are: ")
    elif total_money == 1:
        print(str(total_money) + " cent is: ")
    else:
        print("Please enter a value greater than or equal to one.")
        return
    
    quarters, dimes, nickels, pennies = calculate_coins(total_money)
    
    print_coins(quarters, "quarter")
    print_coins(dimes, "dime")
    print_coins(nickels, "nickel")
    print_coins(pennies, "penny")

main()