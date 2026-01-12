# All capital letters
name = "rohon"
print(name.upper()) # ROHON

# All lower letter
line = "HEllO"
print(line.lower()) # hello

# First letter of all strings to capital letter
line2 = "mashruf mahabub"
print(line2.title()) # Mashruf Mahabub

# check if all letter of a string is lowercase or uppercase
print(name.islower()) # True
print(line.isupper()) # False

# to check if a string contains only characters and not empty
alpha = "Hi there"
print(alpha.isalpha()) # False, cause the string has a space

# to check if a string contains charaters or digit and not empty
alpha_num = "hello6"
print(alpha_num.isalnum()) # True

# to check if a string contains all digits and not empty
decimal = "1234"
print(decimal.isdecimal()) # True


# to check if a string starts with a specific substring
st = "Hello World"
print(st.startswith("Hello")) # True

# to check if a string starts with a specific substring
st2 = "Hello World"
print(st.endswith("World")) # True


# to replace a part of a string
st3 = "Hello World"
st4 = st3.replace("World","Rohon")
print(st4) # Hello Rohon

# to split a string on a specific character seperator
spl = "hi there, Rohon"
print(spl.split(",")) # ['hi there', ' Rohon']

# to trim whitespace from a string
trm = "  Rohon  "
print(trm.strip()) # Rohon

# to append new letters to a string
words = ["Python", "is", "fun"]
result = " ".join(words)
print(result) # Python is fun

chars = ['p', 'y', 't', 'h', 'o', 'n']
result = "".join(chars)
print(result) # python


# to find a position of a substring
sub = "Hi there"
print(sub.find("h")) # 4


# to find the length of a string
print(len("Hello")) # 5


# to find a substring inside a string using 'in'
full_string = "Bangladesh"
print("la" in full_string) # True