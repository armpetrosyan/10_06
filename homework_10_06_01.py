# question 2 // every else besides line 5 and 26, is a string which is inserted into another string


# assigns the variable 10
types_of_people = 10

# a string is assigned to a variable which has a formatted string
x = f"There are {types_of_people} types of people."

# a string is assigned to a variable
binary = "binary"
# a string is assigned to a variable
do_not = "don't"
# a string is assigned to a variable which has two formatted strings
y = f"Those who know {binary} and those who {do_not}."

# these both print out strings which have formatted strings in them
print(x)
print(y)

# these both print out strings which have formatted strings in them
print(f"I said: {x}")
print(f"I also said: '{y}'")

# a boolean value has been assigned
hilarious = False
# a string has been assigned to a variable
joke_evaluation = "Isn't that joke so funny?! {}"

# prints a string which has a formatted boolean value (turned into a string)
print(joke_evaluation.format(hilarious))

# w is assigned a string
w = "This is the left side of..."
# e is assigned a string
e = "a string with a right side."

# concatenation between two strings attaches them together
print(w + e)
