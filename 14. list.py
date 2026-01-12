# A List is a collection which is ordered and changeable. Allows duplicate members.

dogs = ['Roger', 'Syd']

# list can have different type of values and data types
mixed = ['Orange', 1, True, 'Rohon']

# check if a value in the list
print('Rohon' in mixed) # True

# reference item of a list by index
print(mixed[0]) # Orange

# update an element of the list
mixed[3] = "Mango"
print(mixed[3]) # Mango

# last item of the list
print(mixed[-1]) # Mango

# extract part of a list
lis = ['a', 'b', 'c', 'd', 'e', 'f']
print(lis[2:4]) # ['c', 'd']
print(lis[2:]) # ['c', 'd', 'e', 'f']
print(lis[:3]) # ['a', 'b', 'c']

# index of an element
print(f'index of c is {lis.index('c')}') # index of c is 2

# how many item in the list
print(len(lis)) # 6

# add item to a list
lis.append('z')
print(lis) # ['a', 'b', 'c', 'd', 'e', 'f', 'z']

# adding a list with a list
lis.extend(['x', 's'])
print(lis) # ['a', 'b', 'c', 'd', 'e', 'f', 'z', 'x', 's']

# remove from list
lis.remove('a')
print(lis) # ['b', 'c', 'd', 'e', 'f', 'z', 'x', 's']


# remove last item by pop
print(lis.pop()) # s. It is removing the last item and returning 
print(lis) # ['b', 'c', 'd', 'e', 'f', 'z', 'x']

# insert item in a specific index
lis.insert(0, 'y')
print(lis) # ['y', 'b', 'c', 'd', 'e', 'f', 'z', 'x']


# sort a list
lis.sort()
print(lis) # ['b', 'c', 'd', 'e', 'f', 'x', 'y', 'z']

# reverse sort
lis.sort(reverse=True)
print(lis) # ['z', 'y', 'x', 'f', 'e', 'd', 'c', 'b']

# reverse a list
lis.reverse()
print(lis) # ['z', 'y', 'x', 'f', 'e', 'd', 'c', 'b']

# copy of a list
copy_list = lis[:]
print(lis) # ['b', 'c', 'd', 'e', 'f', 'x', 'y', 'z']
print(copy_list) # ['b', 'c', 'd', 'e', 'f', 'x', 'y', 'z']