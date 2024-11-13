'''
## Exercise 8: Simple Search - 30 Marks

Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.
'''
### ANSWER: ###

# List of strings with the specific names stated in the instruction
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# A variable for the name to search for
sam = "Sam"

# If-else to check if "Sam" is in the list
if sam in names:
    print("Sam is in the list.")
else:
    print("Sam is not in the list.")

### ANSWER for Optional Requirements: ###

# List of strings with the specific names stated in the instruction
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# A variable for the name to search for and put input instead of "Sam"
find_name = input("Enter a name to search for in the list: ")

# If-else to check if the input is in the list
if find_name in names:
    print(f"{find_name} is in the list.") # use f string to replace with the value of variable (user input)
else:
    print(f"{find_name} is not in the list.")