print("Let's practice.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
....
\n\t\twhere there is none.
"""

print("-----------")
print(poem)
print("------------")


five =10-2+3-6
print(f"This should be five: {five}")

def secret_formula(startwith):
    jelly_beens = startwith * 500
    jars = jelly_beens / 1000
    crates =jars / 100
    return jelly_beens, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

# another way to format a cooked_string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" cooked_string
print(f"We'd have {beans}, beans, {jars}, jars and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way after dividing the starting_point with 10: ")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format a string
print("We'd have {} jelly_beens, {} jars, and {} crates.".format(*formula))
