#Abdullah Sultan
#Dr. Sudarsky, Block 6
#5/5/2025, 9:45PM
#I hjave neither given nor received any unauthorized aid on this lab
#This lab decyrpts a unique message that has been encrypted with the caesar shift.

def get_message():  
    # opens the encrypted message file and reads its contents  
    
    file = open("/home/amsultan/documents/documents/coding/survey-intro/programming/unit 5/lab3/abdullahsultan.txt", "r")  
    
    message = file.read()  # stores the entire file content as a string  
    
    file.close()  # closes the file to free up system resources  
    
    return message  # returns the encrypted message for decryption  

def decrypt_char(c, shift):  
    # takes a single character (c) and a shift value, then decrypts it  
    
    num = ord(c)  # converts the character to its ascii number (e.g., 'a' → 97)  
    # shifts the ascii value down by 32 to normalize it (since printable chars start at 32)  
    # subtracts the shift to reverse the encryption, then wraps around using % 95  
    # adds 32 back to return to the original ascii range (32–126)  
    
    new_num = (num - 32 - shift) % 95 + 32  
    
    return chr(new_num)  # converts the new ascii number back to a character  

def try_shifts(message):  
    
    # tries every possible shift from 51 to 100 and builds the decrypted results  
    result = ""  # stores all decrypted attempts as one big string  
    
    for shift in range(51, 101):  # loops through shifts -51 to -100  
        decrypted = ""  # stores the current shift's decrypted message  
        
        for char in message:  # processes each character in the encrypted message  
            decrypted += decrypt_char(char, shift)  # decrypts and adds to the string  
        # adds the shift label and decrypted text to the final result  
        
        result += "shift -" + str(shift) + ":\n" + decrypted + "\n\n"  
    
    return result  # returns all decryption attempts  

def save_to_file(text):  
    
    # saves the decrypted results to a file  
    file = open("/home/amsultan/documents/documents/coding/survey-intro/programming/unit 5/lab3/decrypt.txt", "w")  
    
    file.write(text)  # writes the full decrypted output to the file  
    
    file.close()  # closes the file  

def main():  
    # runs the full decryption process  
    
    secret = get_message()  # gets the encrypted message from the file  
    
    decrypted = try_shifts(secret)  # tries all shifts and stores results  
    
    save_to_file(decrypted)  # saves the results to decrypt.txt  

main() 