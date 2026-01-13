# While 

count = 1

while count <= 10:
    print("Condition is true")
    count += 1

print("After the loop")

"""
Condition is true
Condition is true
Condition is true
Condition is true
Condition is true
Condition is true
Condition is true
Condition is true
Condition is true
Condition is true
After the loop
"""


# for

items = [1, 2, 4, 5, 6]

for item in items:
    print(item)

"""
1
2
4
5
6
"""


# range
for item in range(15):
    print(item) # 0-14




# getting index
items = [1, 2, 4, 5, 6]

for index, item in enumerate(items):
    print(f'for index {index} item is {item}')

"""
for index 0 item is 1
for index 1 item is 2
for index 2 item is 4
for index 3 item is 5
for index 4 item is 6
"""


# printing even numbers

for item in range(2, 10, 2):
    print(item) # 2 4 6 8

"""
- It will run from 1 to 10.
- Adding 2
"""



# reverse a loop

for item in range(10, 0, -1):
    print(item)

"""
10
9
8
7
6
5
4
3
2
1
"""