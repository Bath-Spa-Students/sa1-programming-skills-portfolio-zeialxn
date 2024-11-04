'''
## Exercise 4: Primitive Quiz - 30 Marks

In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.

'''

# Answer

answer = (input("What is the capital of France? Answer: "))
if answer == "Paris":
    print("Your answer is correct!")
elif answer == "paris":
    print("Your answer is correct!")
else:
    print("Your answer is incorrect.")

'''
Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.
'''

# Ignore Capitalization
answer = (input("What is the capital of France? Answer: ")).lower()
if answer == "paris":
    print("Your answer is correct!")
else:
    print("Your answer is incorrect.")

# Multiple Questions
print("Name the Capital of 10 European Countries")

first = (input("What is the capital of Austria? Answer: ")).lower()
if first == "vienna":
    print("Your answer is correct!")
else:
    print("Your answer is incorrect.")

second = (input("What is the capital of Germany? Answer: ")).lower()
if second == "berlin":
    print("Your answer is correct!")
else:
    print("Your answer is incorrect.")

third = (input("What is the capital of Ireland? Answer: ")).lower()
if third == "dublin":
    print("Your answer is correct!")
else:
    print("Your answer is incorrect.")

fourth = (input("What is the capital of Italy? Answer: ")).lower()
if fourth == "rome":
    print("Your answer is correct!")
else:
    print("Your answer is incorrect.")

fifth = (input("What is the capital of Netherlands? Answer: ")).lower()
if fifth == "amsterdam":
    print("Your answer is correct!")
else:
    print("Your answer is incorrect.")

sixth = (input("What is the capital of Portugal? Answer: ")).lower()
if sixth == "lisbon":
    print("Your answer is correct!")
else:
    print("Your answer is incorrect.")

seventh = (input("What is the capital of Russia? Answer: ")).lower()
if seventh == "moscow":
    print("Your answer is correct!")
else:
    print("Your answer is incorrect.")

eigth = (input("What is the capital of Spain? Answer: ")).lower()
if eigth == "madrid":
    print("Your answer is correct!")
else:
    print("Your answer is incorrect.")

ninth = (input("What is the capital of Switzerland? Answer: ")).lower()
if ninth == "bern":
    print("Your answer is correct!")
else:
    print("Your answer is incorrect.")

tenth = (input("What is the capital of United Kingdom? Answer: ")).lower()
if tenth == "london":
    print("Your answer is correct!")
else:
    print("Your answer is incorrect.")





