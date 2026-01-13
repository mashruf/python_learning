'''
An exception is an error that occurs during the execution of a program. 
When Python encounters an error it doesn’t know how to handle, 
it stops the program and shows a traceback.

Example:
x = 5 / 0
ZeroDivisionError: division by zero

Build-in exceptions we may often see
| Exception           | When it occurs                                                         |
| ------------------- | ---------------------------------------------------------------------- |
| `ZeroDivisionError` | Dividing a number by zero                                              |
| `ValueError`        | Passing a wrong type of value (e.g., converting letters to int)        |
| `TypeError`         | Performing an invalid operation between types (e.g., adding int + str) |
| `IndexError`        | Accessing an index that doesn’t exist in a list                        |
| `KeyError`          | Accessing a key that doesn’t exist in a dictionary                     |
| `FileNotFoundError` | Trying to open a file that doesn’t exist                               |
| `NameError`         | Using a variable that hasn’t been defined                              |

'''

# Handling Exceptions with try and except
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That’s not a valid number!")
else:
    print("Result is:", result)
finally:
    print("This runs no matter what.")


'''
try: Code that might raise an exception.

except: Handles the exception if it occurs.

else: Runs if no exception occurred.

finally: Runs always, even if there was an exception. Good for cleanup (like closing files).
'''

# Catching Multiple Exceptions at Once
try:
    x = int(input("Enter a number: "))
    result = 10 / x
except (ZeroDivisionError, ValueError) as e:
    print("Error:", e)


"""
You can stop the program manually if something goes wrong using raise.
"""
age = -3
if age < 0:
    raise ValueError("Age cannot be negative!")


"""
Raising and Handling Together
"""
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative!")
except ValueError as e:
    print("Caught an error:", e)

print("Program continues running")




"""
Rais + Handle the custom exception
"""
class InvalidAgeError(Exception):
    pass

try:
    age = -10
    if age < 0:
        raise InvalidAgeError("Age cannot be negative!")
    print("Age is:", age)

except InvalidAgeError as e:
    print("Custom Error:", e)

print("Program continues")
