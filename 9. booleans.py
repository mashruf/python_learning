"""
booleans has two values, True and False
"""

done = True

if done:
    print("yes") # yes. 
else:
    print("no")

"""
It prints yes because done = True. 
It will print no if done = False.

Falsy value in python:
- None and False
- 0 (integer zero)
- 0.0 (float zero)
- '' or "" (empty string)
- [] (empty list)
- () (empty tuple)
- {} (empty dictionary)
- set() (empty set)
- range(0) (empty range) 
"""




"""
any() returns True if any item in the provided iterable is "truthy",
and False otherwise.
"""
my_list = [0, False, "", 5]
print(any(my_list)) # True


"""
all() returns True if all item in the provided iterable is "truthy",
and False otherwise.
"""
my_list2 = [1, 2, 3, True, 5]
print(all(my_list2)) # True