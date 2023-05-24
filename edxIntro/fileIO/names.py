"""names = []

for _ in range(3):
    name = input("Waht's your name? ")
    names.append(name)

for name in sorted(names):
    print(f"hello, {name}")"""

name = input("What's your name? ")

### WRITE to file
#file = open("names.txt", "a")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
#file.close()

## READ the file
with open("names.txt", "r") as file:
    for line in file:
        # lines = file.readlines()
        print("hello,", line.rstrip())


# for line in lines:
#    print("hello,", line.rstrip())
    
