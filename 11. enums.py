"""
Enum is a type that holds a small set of named, fixed choices.
Enum = a list of allowed options with names.
"""

from enum import Enum


# Make the enum(The menu of allowed values)
class Light(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

print(Light.RED.name) # RED
print(Light.RED.value) # 1


"""
Enum = a box of buttons
You can only press the buttons in the box: RED, YELLOW, GREEN
"""

# to use all the values of an enum
print(list(Light)) # [<Light.RED: 1>, <Light.YELLOW: 2>, <Light.GREEN: 3>]

# to find the length of an enum
print(len(Light))