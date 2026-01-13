'''
Every python file is a module

We can import a module from any file
'''


'''
we have created a python file called dog.py

we can use all the method created on that file

import dog # it will allow us to use all the method in dog.py file
dog.bark() # we are using the bark() method from dog.py file
'''


#or

'''
from dog import bark # We will only able to use bark() method

bark()
'''


'''
If we create a module inside a sub folder, then we have to create a file 
inside the sub folder called __init__.py

This file tells python that the folder contains python module
'''



'''
We have a folder called lib

Inside lib, we have module called dog.py and the module has a method called bark()

if we want to import the dog module:
from lib import dog

if we want to import only the bark() method
from lib.dog import bark
'''



#  using python standard library

import math

print(math.sqrt(4)) # 2.0