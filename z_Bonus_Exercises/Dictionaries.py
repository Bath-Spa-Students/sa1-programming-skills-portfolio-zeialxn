'''
Use a dictionary to store information about a person you know.Store their first name,
last name, age, and the city in which they live.

You should have keys such as first_name, last_name, age, and city. Print each piece of
information stored in your dictionary.
'''

# dictionary about a person i know
information = {"first_name": "Axl",
               "last_name": "Soriano",
               "age": 19,
               "city": "Valenzuela"}
# print each piece of information
for key, value in information.items():
    print(f"{key}: {value}")