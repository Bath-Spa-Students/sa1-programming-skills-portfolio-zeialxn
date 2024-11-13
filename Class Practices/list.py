# Homogeneous List / Python Suppports Heterogeneous List othe
names = ["Zhealene", "Eihra", "Lucero"]
print(names)
countries = ["Philippines", "United Arab Emirates", "South Korea"]
print(countries)
fruits = ['Apple', 'Banana', 'Kiwi']
print(fruits)

# Hetrogeneous List
Student = ["Zhealene", 143, 3.14]
print(Student)
order = ['Burger', 15, 2.50]
print(order)
color = ['Red', 913831, 9.13831]
print(color)

# Repetition operator
numbers = [1, 2, 3, 4]
new_numbers = numbers * 2
print(new_numbers)
colors = ['Red', 'Orange', 'Yellow']
new_colors = colors * 5
print(new_colors)
even = [2, 4, 6, 7, 8]
new_even = even * 8
print(new_even)
decimal = [2.15, 4.98, 3.58]
new_decimal = decimal * 2
print(new_decimal)

# Positive Indexing
# —> starts from 0, left to right
numbers =[5,6,7,8,3,4]
print(numbers[3]) 

# Negative Indexing
# —> starts from -1 bcz 0 is a non-negative integer, right to left
numbers =[5,6,7,6,3,4]
print(numbers[-3])

# lens function tells us number of items in the list 
numbers =[5,6,7,8,3,4]
print("number of elements in a list :" ,len(numbers))

# Mutability (Changable) we can change values in the list 
numbers =[5,6,7,8,3,4]
numbers[0]=1
    #[index]=the number you wanna replace/put

#Concatenation Dont use small "l" (list) to write variable name eg (list )
List_1 =[2,3,4,5,6]
List_2=[9,8,7,6,5]
#Concatenation through + operator
List_3=List_1 + List_2
print (List_3)

# List slicing  - to use one part of list 
new_list =[1,2,3,10,15,6,7]
result= new_list [0:3] # 2nd index exclusive index - 0-2 index , total 3 elements  , [3:7] 1st index inclusive
print(result)

# find elements in list  -if operator 
new_list1 =[1,2,3,5,6,7,8,9]
if 10 in new_list1:
     print("found")
else:
      print ("Not found")

# (not in)  operator 
new_list2 =[1,2,3,5,6,7,8,9]
if 20 not in new_list2:
     print("yes")
else:
      print ("No")

# built in methods - append
New_list3 = [4,5,6,6,7]
New_list3.append(100)
print (New_list3) 

#   built in methods - index
New_list4 = [4,5,6,6,7]
print (New_list3.index(7))  # Identify index of number 7

#   built in methods - sort
New_list5 = [4,7,6,3,1]
New_list5.sort()
print(New_list5)     

#   built in methods - reverse
New_list6 = [4,7,6,3,1]
New_list6.reverse()
print(New_list6)

#   built in methods - remove
New_list7 = [4,7,6,3,1]
New_list7.remove(6)
print(New_list7)