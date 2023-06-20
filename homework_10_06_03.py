# the variable is assigned a strings which holds 4 f-string brackets
formatter = "{} {} {} {}"
# using the function .format, these 4 decimal arguments are passed into those brackets
print(formatter.format(1, 2, 3, 4))
# using the function .format, these 4 string arguments are passed into those brackets
print(formatter.format("one", "two", "three", "four"))
# using the function .format, these 4 boolean arguments are passed into those brackets
print(formatter.format(True, False, False, True))
# using the function .format, these 4 arguments are placed accordingly into the brackets(prints 16 brackets)
print(formatter.format(formatter, formatter, formatter, formatter))
# using the function .format, these 4 string arguments are passed into those brackets
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
 ))
