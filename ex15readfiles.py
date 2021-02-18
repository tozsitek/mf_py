from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}: ")
print(txt.read())
txt.close()

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)
# might need to do this
# txt_again = open(file_again, encoding="utf-8")

print(txt_again.read())
txt_again.close()
