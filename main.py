# # print(2 + 3)

print ('Hello World!!')

print('Goodbye!')


# Data Types

# Numbers

# int
# 5
# 1000
print(type(5))

# float
# 2.2
# 5.1
# 3.14159
print(type(3.14159))

# complex
# 2 + 3j
print(type(2+3j))

# Number operations
print(2+3)
print(2-3)
print(5 * 2) # Multiplication
print(10 / 5) # Float division
print(10 // 3.5) # Integer division ... sometimes
print(5 % 2) # Modulo (remainder)
print(int(10 // 3.5)) # Integer division (with typecast)

# Strings
# "Hello World!!"
# 'Hello World!!' 

      # How to instruct Python to instruct apostrophe
print('It\'s Monday!') # Escaping (escape the normal way Python would intepret this character)

# Concatenation
print('Hello ' + 'World!')

# String methods
print('Hello'.upper())
print('Hello World'.replace('World', 'There'))

# Falsy values
print(bool('0')) # Evaluates as False
print(bool('')) # Empty string - evaluates as False
print(bool('ghfha')) # Evaluates as True 

# String methods
print('hello' .upper())
print('Hello World' .replace ('World', 'There')) # Replaces

# Boolean Values
# True
# False
print(type(True))
print(bool(0))
print(bool(''))
print(bool(None))
print(bool([]))
print(bool(()))
# print(bool({}))

# Comparison operators
# <,>, <=, >=, ==
print(2 < 3)
print(5 <= 5)

# Logical operators
# and, or, not
print(True and False) # Evaluates as False
print(False or True) # Evaluates as True
print(5 > 3 and 2 < 5) # Evaluates as True

# Variables # An area of memory that has a label attached to it
num1 = 5
num2 = 4
print(num1 + num2)
num2 = 10 # Changes the original value
print(num1)
print(num2)

# String interpolation
name = "Wangari"
# f-string
print(f'My name is  {name}  and I live in Melbourne')