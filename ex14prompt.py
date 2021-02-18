from sys import argv
script, user_name = argv
#prompt = '> '
prompt = f'{script} ({user_name})>'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions. ")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"How old are you {user_name}?")
age = int(input(prompt))

# it's only a sample, don't do int conversion here, but rather on line 15
print(f"You are {int(age)} year old. What kind of computer do you have?")
computer = input(prompt)
print(f"""
All right, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
You are {age} year young.
And you have a {computer} computer. Nice.""")
