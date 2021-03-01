
class Dog:
    # pass

    # class Attribute
    species = "Canis familiaris"


    # instance attrributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

buddy = Dog("Buddy", 9)
print(buddy.description())
print(buddy.speak('Gruff!!!!'))
print("**********************************")

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print("Wait, there are not 10 items in the list, we need to fix it")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding one: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)
print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
