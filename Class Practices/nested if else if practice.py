
earning = int(input("Enter your earning per year: "))
Work_Experience = float(input("Enter your work experience: "))

if earning >= 30000:
    if Work_Experience >= 2:
        print("Eligible for loan.")
    else:
        print("Sorry, your work experience is less than 2 years.")
else:
    print("Sorry, your earning is less than 30,000.")