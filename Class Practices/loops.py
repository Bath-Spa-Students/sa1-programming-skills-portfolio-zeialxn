# Lets suppose i want to Print 10 numbers - as per previous practices -
# Through print functions ,  line by line Is it a Good practice ?
# Lets suppose i need to print hundred values ?
# If condition True then Loop Sarts 
# What happens if the condition not false - infinite loop 
# 80 % For Loop Use in loops , also named as counter control loop 

#While Loop 
# 

# https://www.w3schools.com/python/python_while_loops.asp

# With the while loop we can execute a set of statements as long as a condition is true.
# Print j as long as j is less than 10:

i = 5
while i < 10:
    print(i)
    i+=1 #i =i+1

count = 1
while count <= 5:
    print("Count is:", count)
    count += 1 #increment

#Infinite Loop With Break Statement 

j = 1
while j < 6:
  print(j)
  if j == 3:
    break
  j += 1   # j=j+1  Both are same 