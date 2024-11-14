#Local variable

def function_name():
    local_variable = "Hello!"
    print(local_variable)

#calling function
function_name()

#Different functions have same local variable name but no syntax error

def function_name():
    local_variable = "Hello!"
    print(local_variable)

def function_name_2():
    local_variable = "Hi!"
    print(local_variable)

function_name()
function_name_2()