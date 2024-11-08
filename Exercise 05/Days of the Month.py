'''
## Exercise 5: Days of the Month - 30 Marks

Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.

### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.
'''

### Answer: ###
months = {1: 31,
          2: 28/29,
          3: 31,
          4: 30,
          5: 31,
          6: 30,
          7: 31,
          8: 31,
          9: 30,
          10: 31,
          11: 30,
          12: 31}

try:
    month_number = int(input("Enter a month number: "))

    if 1 <= month_number <= 12:
        print(f"The month {month_number} has {months[month_number]} days.")
    else:
        print("The number is invalid.")
        print("Please enter a number between 1 and 12 only.")

except ValueError:
    print("The input is invalid.")
    print("Please enter a valid integer.")

### Answer for Advanced Requirements: ###

months = {1: 31,
          2: 28,
          3: 31,
          4: 30,
          5: 31,
          6: 30,
          7: 31,
          8: 31,
          9: 30,
          10: 31,
          11: 30,
          12: 31}

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

try:
    month_number = int(input("Enter a month number: "))
    year = int(input("Enter the year: "))

    if 1 <= month_number <= 12:
        if month_number == 2:
            if leap_year(year):
                print(f"The month {month_number} in the year {year} has 29 days.")
            else :
                print(f"The month {month_number} in the year {year} has 28 days.")
        else:
            print(f"The month {month_number} has {months[month_number]} days.")
    else:
        print("The number is invalid.")
        print("Please enter a number between 1 and 12 only.")
except ValueError:
    print("The input is invalid.")
    print("Please enter a valid integer.")