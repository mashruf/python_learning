name = "Rohon" # String


"""
To know the type of a variable we use type()
""" 
print(type(name)) # <class 'str'>



"""
Checking the instance of the variable 
whether it is str or not
"""
print(isinstance(name, str)) # True



number = 3 # Integer
print(isinstance(number, int)) # True


age = 2.9 # Float
print(isinstance(age, float)) # True



"""
- We can convert type of a variable
to other.
- It is called type casting.
- We can convert int to float, float to int, string to int etc
"""
num = "20"
print(isinstance(num, int)) # False

convert_num_to_int = int(num)
print(isinstance(convert_num_to_int, int)) # True

"""
But we will get error if 
we try to convert following string value to int or float
"""
number = "Test"
convert_number_to_int = int(number)
print(convert_number_to_int) # Error





"""
There are few other types:
complex for complex numbers
bool for booleans
list for lists
tuple for tuples
range for ranges
dict for dictionaries
set for sets
"""



