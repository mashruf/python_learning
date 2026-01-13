def hello():
    print("Hello")

hello() # Hello


# function can have more than one parameter
def hello(name):
    print(f'Hello {name}')

hello('Rohon') # Hello Rohon


# default parameter
def hello(name='My friend'):
    print(f'Hello {name}')

hello() # Hello My friend


# return
def hello(name):
    return f'Hello {name}'

print(hello('Rohon')) # Hello Rohon