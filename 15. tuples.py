"""
- A Tuple is a collection which is ordered and unchangeable.
- Allows duplicate members.
- Once a tuple is created, it can not be modified.
- We can not add or remove items.
- Tuple is ordered
- Can have duplicate value
"""


tup = ('Mashruf', 'Rohon')

# referencing a value by index
print(tup[0]) # Mashruf

# index of an element
print(tup.index('Rohon')) # 1

# last index value
print(tup[-1]) # Rohon

#how many item in the tuple
print(len(tup)) # 2

# if an element is in a tuple
print("Mashruf" in tup) # True

# slice 
print(tup[0:1]) # ('Mashruf',)

# Add single value in a tuple
tup += ("Mahabub",) # must have , for single element
print(tup) # ('Mashruf', 'Rohon', 'Mahabub')

# Add multiple values
tup += ("Sarah", "Ali")
print(tup) # ('Mashruf', 'Rohon', 'Mahabub', 'Sarah', 'Ali')



