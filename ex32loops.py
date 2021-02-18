the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots',]
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count: {number}")

for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go throug mixed lists # too
# notice we have to user {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we cna also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
    print(f"Adding {i} to the list.")
    # append is a fucntion that lists understand
    elements.append(i)

print(">>>> elements: ", repr(elements))
print(">>>> after loop i= ", i)

# make a copy of the elements
copyOfElements = elements[:]
for i in elements: print("the copy is: ", i)

# creating a range and listing it on the command line
# list(range(0,22))
# going down by 2 starting with 1k
# list(range(1000,100,-2))


#now we can print tem out too
for element in elements:
    print(f"Element was: {element}")

for j in elements: print(j)
