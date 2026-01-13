"""
Global variable: Can be used in anywhere of code
"""
age = 8

def print_age():
    print(age) # we can access the variable age because it is declared out of the function

print(age) # 8
print_age() # 8


"""
Local variable: Can be used only inside a block
"""

def print_name():
    name = "Roger"
    print(name)

print(name) # error because name is not global
print_name()