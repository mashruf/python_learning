'''
Change each item” → use map → returns an iterator of transformed items

Keep some items” → use filter → returns an iterator of items that passed the test

Combine all items” → use reduce → returns one final combined value
'''


# map()

'''
using normal function:

numbers = [1,2,3,4]

def double(a): # function that multiply number with 2
    return a*2

result = map(double, numbers)

# we have to convert the result into list
print(list(result)) # [2, 4, 6, 8]
'''


'''
using lamda function:

numbers = [1,2,3,4]

double = lambda a : a * 2

result = map(double, numbers)

# we have to convert the result into list
print(list(result)) # [2, 4, 6, 8]
'''


'''
shorter with lamda function:

numbers = [1,2,3,4]

result = map(lambda a : a * 2, numbers)

# we have to convert the result into list
print(list(result)) # [2, 4, 6, 8]

'''




# filter()

num = [1,2,3,4,5,6]

res = filter(lambda a : a % 2 == 0, num)

print(list(res))  # [2, 4, 6]



# reduce()

'''
reduce always works with two values at a time, usually written as a and b

a = the accumulated result so far

b = the next item from the list
'''

from functools import reduce

nums = [10, 33, 53, 66, 21]

result = reduce(lambda a, b: a + b, nums)

print(result) # 183