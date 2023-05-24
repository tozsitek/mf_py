names = []


## variety of sorting
with open("names.txt", "r") as file:
    for line in file:
        #lines = file.readlines()
        #print("hello,", line.rstrip())
        names.append(line.rstrip())
        
# list the file sorted
for name in sorted(names, reverse=True):
    print(f"hello, {name}")
    
"""with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())"""
