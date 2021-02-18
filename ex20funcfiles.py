from sys import argv

script, input_file = argv

def print_all(f):
    # print(">>> print_all file", f)
    print(f.read())
    # print("<<< print_all file", f)

def rewind(f):
    f.seek(0)

# adding end="" makes sure the lines are printed right one after another, no empty lines
# displayed
def print_a_line(line_count, f):
    print(line_count, f.readline(), end="")

current_file = open(input_file)
print("First let's print the whole file:")
print_all(current_file)
# this won't print anything as we're at the end of the file
# print("print the file again: ")
# print_all(current_file)

print("Now let's rewind: ")
rewind(current_file)

print("Let's print 2 lines: ")
current_line = 1
print_a_line(current_line, current_file)
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

current_file.close()
