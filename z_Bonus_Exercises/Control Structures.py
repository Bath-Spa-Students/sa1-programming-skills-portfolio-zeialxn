'''
Imagine an alien was just shot down in a game. Create a variable called alien_color and
assign it a value of 'green', 'yellow', or 'red'.
•Write an if statement to test whether the alien’s color is green. If it is, print a message
that the player just earned 5 points.
•Write one version of this program that passes the if test and another that fails. (The
version that fails will have no output.)

'''

# create a variable and assign a value
alien_color = "red"

# if statement to test whether the alien’s color is green
if alien_color == "green":
    # if it is, print a message that the player just earned 5 points
    print("You just earned 5 points!") # no output because it failed the if test

# another version of this program that passes the if test
if alien_color == "red":
    print("You just earned 5 points!")