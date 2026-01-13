# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

dog = {
    "name": "Roger",
    "age":8
    }

# access individual key value
print(dog['name']) # Roger

# changing value
dog['name'] = "Syd"
print(dog) # {'name': 'Syd', 'age': 8}

# accessing value by get
print(dog.get('name')) # Syd



"""
we can add default value for an item which 
is not present in the dict
"""
# print(dog['color']) # error
# we will write the following to eliminate the error
print(dog.get('color')) # None
# we will write following to set value of a key which is not currently in the dict
print(dog.get('color', 'black')) # black


# delete an item from dict
print(dog.pop('name')) # Syd
print(dog) # {'age': 8}


# remove last item
dog = {
    "name": "Roger",
    "age":8,
    "color": "green" 
    }

dog.popitem()
print(dog) # {'name': 'Roger', 'age': 8}

# check if an item in dict
print('name' in dog) # True

# get all keys
print(dog.keys()) # dict_keys(['name', 'age'])
# convert into list
print(list(dog.keys())) # ['name', 'age']


# get all values
print(dog.values()) # dict_values(['Roger', 8])
# convert into list
print(list(dog.values())) # ['Roger', 8]



# get all items and convert them into list
print(list(dog.items())) # [('name', 'Roger'), ('age', 8)]



# how many items
dog = {
    "name": "Roger",
    "age":8,
    "color": "green" 
    }
print(len(dog)) # 3



# add new item
dog["food"] = "Meat"
print(dog) # {'name': 'Roger', 'age': 8, 'color': 'green', 'food': 'Meat'}


# delete an item
del dog["food"]
print(dog) # {'name': 'Roger', 'age': 8, 'color': 'green'}

# copy a dict
dog2 = dog.copy()
print(dog2) # {'name': 'Roger', 'age': 8, 'color': 'green'}