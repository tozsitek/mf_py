from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
#first, second, third = argv

print(">>> argv is: ", repr(argv))

#print("The script is called: ", script)
print("The first variable, second argument: ", first)
print("The second variable, third argument: ", second)
print("The third variable, fourth argument: ", third)
