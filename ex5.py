my_name = 'Marianna ala tozsi'
my_fName = 'Marianna'
my_lName = 'Fields'
my_age = 44
my_height = 78 # inches
my_weight = 135
my_eyes = 'grey'
my_teeth = 'quite white'
my_hair = 'brown'

print(f"Let's talk about {my_name}.")
print(f"She is {my_height} inches tall.")
print(f"She's {my_weight} pounds light.")
print(f"Actually that's not heavy at all.")
print(f"She's got {my_eyes} eyes and {my_hair} hair.")
print(f"Her teeth are usually {my_teeth} depending on the coffee.")
print(f"Add {str(my_age) + my_eyes}: age and eyes.")
print(f"My full name is: {my_fName + ' ' + my_lName}")

# this line is tricky to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} together, I get {total}.")
