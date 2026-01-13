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
