'''
Python decorators are a short way to wrap a function with extra behavior—without changing the function’s code.

Basic idea:
A decorator is a function that takes another function and returns a new one.
'''

def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hi():
    print("Hi")

say_hi()
