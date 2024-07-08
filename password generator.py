import string
import random
 

length = int(input("Enter password length: "))
 
print('''Choose character set for password from these : 
         1. Digits
         2. Letters
         3. Special characters
         4. Exit''')
 
characterList = ""
 
6
while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
         
        
        characterList += string.ascii_letters
    elif(choice == 2):
         
        
        characterList += string.digits
    elif(choice == 3):
         
        
        
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")
 
password = []
 
for i in range(length):
   
    # Picking a random character from our 
    # character list
    randomchar = random.choice(characterList)
     
    # appending a random character to password
    password.append(randomchar)
 
# printing password as a string
print("The random password is " + "".join(password))
