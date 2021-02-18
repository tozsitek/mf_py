#this one is like the scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is acrually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this takes only one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no argument
def print_none():
    print("I got nothing.")

print_none()
print_two("Marianna", "Anett")
print_two_again("Marianna", "Anett")
print_one("Only one")
