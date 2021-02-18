i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i+1
    print("Numbers after append is: ", numbers)
    print(f"At the bottom i is: {i}")


print("The numbers after the while loop: ")

for num in numbers:
    print(num)    
