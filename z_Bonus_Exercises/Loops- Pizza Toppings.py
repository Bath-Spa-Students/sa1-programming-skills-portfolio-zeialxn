'''
Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza.
'''
# input to allow user to enter toppings or quit value
while True:
    pizza_toppings = input('Enter a pizza topping or enter "QUIT" to stop: ')
    
    # loop will break if the user enter a quit value
    if pizza_toppings.upper() == "QUIT": # this converts the input to upper case
        print("Thank you, your order is coming right up!")
        break
    # the message will be dispayed as the user enters a pizza topping
    else:
        print(f"Noted! We'll add {pizza_toppings} on your pizza.")