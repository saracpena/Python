#
# Example file for variables
#

# Declare a variable and initialize it
f = 0
# print(f)


# re-declaring the variable works
# f="abc"
# print(f)

# ERROR: variables of different types cannot be combined
#

# Global vs. local variables in functions
def someFunction():
    global f
    f = "def"
    print(f)

someFunction()
print(f)

def f
print(f)