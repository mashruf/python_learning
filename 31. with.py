"""
with in Python is used for automatic resource management — it makes sure things like files, network connections, or locks are properly cleaned up, even if an error happens.

Think of with as:
“Use this thing, and when I’m done, clean it up for me.”
"""

"""
Without with:

file = open("data.txt")
data = file.read()
file.close()   # you MUST remember this
"""


"""
Using with
with open("data.txt") as file:
    data = file.read()

# file is automatically closed here
"""


"""
Using with with multiple things
with open("a.txt") as f1, open("b.txt") as f2:
    print(f1.read())
    print(f2.read())
"""