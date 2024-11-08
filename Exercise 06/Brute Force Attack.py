'''
## Exercise 6: Brute Force Attack - 30 Marks

Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.

### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. If the maximum number of attempts is reached, inform the user that the authorities have been alerted.
'''

### ANSWER for Basic Requirements: ###

correct_password = "12345" 

while True:
    password = input("Enter the password: ")
    if password == correct_password:
        break
    else:
        print("Try again.")

print("Password is correct.")

### ANSWER for Optional Requirements: ###

correct_password = "12345"
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    password = input("Enter the password: ")

    if password == correct_password:
        print("The password is correct.")
        break
    else:
        attempts += 1
        attempts_left = max_attempts - attempts
        if attempts_left > 0:
            print("The password is incorrect. Try again.")
            print(f"You have {attempts_left} attempt(s) remaining.")
        else:
            print("The password is incorrect.")
            print("You don't have any attempts remaining.")
            print("The authorities have been alerted.")
            break