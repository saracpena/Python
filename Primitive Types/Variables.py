import math

# Storing data in the computers memory
# Primitive Types: numbers, booleans, strings
students_count = 1000
# floating
rating = 4.99
is_published = False
course_name = "Python programming"
print(students_count)

course = "Python Programming"
# Function is a reuseable piece of code that carries out a task
# len is a built-in function
# ! length of string
print(len(course))
# ! locate index in string
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])

message = """
Hi Sara,

This is Warner Brothers
"""

# ! ESCAPE SEQUENCES
# \"
course = "Python \"Programming"
print(course)
# \'
course = "Python \'Programming"
print(course)
# \\
course = "Python \\Programming"
print(course)
#  \n = new line
course = "Python \nProgramming"
print(course)

# !=====================
first = "Sara"
last = "Peña"
full = f"{first} {last}"
print(full)
# !Getting the length
first = "Sara"
last = "Peña"
full = f"{len(first)} {last}"
print(full)

# !===========String Methods everything in python are objects
course = "Python Programming"
print(course.upper())
print(course.lower())
print(course.title())
# eliminate white space

print(course.strip())
# finding the index of 'pro'
print(course.find("Pro"))
# replace
print(course.replace("P", "J"))
# replace a character or sequence of character with somehting else, replacing all uppercase p's with j
print(course.replace("P", "J"))
# check for existence of character or sequence of using 'in' operator
# ! boolean
print("Pro" in course)
# 'not in' operator = does not contain charater of sequence of
print("swift" not in course)

# !Numbers ============================ (Integers, Floats, Complex Numbers)
# Add
print(10 + 3)
# Subtract
print(10 - 3)
# Multiply
print(10 * 3)
# Divide
print(10 / 3)
# Divide to produce integer from a floating number
print(10 // 3)
# modulo
print(10 % 3)
# Exponent
print(10 ** 3)

# !=======
x = 10
x = x + 3
x += 3

# ! Built-in MATH Functions ===============
print(round(2.9))
# abs, absolute value
print(abs(2.9))
# ! Import Math above for additional functions
# getting the ceiling of a number which below is 3
print(math.ceil(2.2))

# ! Type Conversion ================
x = input("x: ")
# y = x + 1
y = int(x) + 1
print(f"x: {x}, y: {y}")
