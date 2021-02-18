# assign 10 to types_of_people
types_of_people = 10
# assign the f-string to x (insert types_of_people in the string)
x = f"There are {types_of_people} types of people"
print(types_of_people)

#
binary = "binary"
do_not = "don't"
# assign f-string to y containing (binary) and (do_not) variables
y = f"Those who know {binary} and those who {do_not}."
print(">>>>>>After assignment to y: ", y)

print(x)
print(y)

print(f"I said: {x}")
print(">>>>>>Before printing y: ", y)
print(f"I also said: '{y}'")
print(f"I also said (not formatted): ", y)

hilarious = False
joke_evaluation = "Isn't that joke so funny? {}"
print(joke_evaluation.format(hilarious))

w = "this is the left side of ..."
e = "a string with a right side."
print(w + e)
