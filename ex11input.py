print("How old are you? ", end='')
#age = input()
# print(">>>> age= ", repr(age))  # string
# if you want to collect a number
age = int(input())
print(">>>> age= ", repr(age)) # int
print("How tall are you? ", end='')
height = input()
print("How much do you weigh? ", end='')
weight = input()

print("Age: ", age)
print("Height: ", height)
print("Weight: ", weight)

print(f"So you are {age} years old, {height} tall and {weight} heavy")
