"""
Arithmetic operators

1. 1 + 1 # 2
2. 2 - 1 # 1
3. 2 * 2 # 4
4. 4 / 2 # 2
5. 4 % 3 # 1
6. 4 ** 2 # 16
7. 5 // 2 # 2, we are supposed to get 2.5 but we will get 2(The nearest number of 2.5).
"""



"""
Comparison operator:

a = 5
b = 3


a==b # False
a!=b # True
a>b # True
a>=b # True
a<b # False
a<=b # False
"""



"""
Boolean operators:

and
or
not

- and: Returns True if both operands are True, otherwise False.
    
    print(True and True)   # Output: True
    print(True and False)  # Output: False


- or: Returns True if at least one operand is True, otherwise False
    
    print(True or False)   # Output: True
    print(False or False)  # Output: False

- not: Unary operator that reverses the boolean value of its operand. 
not True is False, and not False is True.

    print(not True)    # Output: False
    print(not False)   # Output: True


or: or using an expression returns the value of the first operand
that is not a false value or falsy value. Otherwise it will return 
the last operand

print(0 or 1) # 1
print(False or 'hey') # hey
print('hi' or 'hey') # hi
print([] or False) # False
print(False or []) # []

We can remember the operation of 'or' by: If x is false, then y, else x

and: and only evaluates the second argument
if the first one is true.

print(0 and 1) # 0
print(1 and 0) # 0
print(False and 'hey') # False
print('hi' and 'hey') # hey
print([] and False) # []
print(False and []) # False

We can remember the operation of 'and' by: If x is False then x else, y.
"""


"""
is & in operators:

- "is" is called the identity operator. It is used to compare to objects
and returns true if both are the same objects

- "in" is called the membership operator. This is used to tell if a value
is in a list or another sequence.
"""


"""
Ternary operator:

def isAdult(age):
    if age>18:
        return True
    else:
        return False

We can write the above code by following:

def isAdult(age):
    return True if age>18 else False
    
"""

