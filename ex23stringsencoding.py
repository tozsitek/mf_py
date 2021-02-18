import sys
script, input_encoding, error = sys.argv

def myencoding(language_file, encoding, errors):
    print(">>> in main before line declaration, before if statement", repr(language_file))
    line = language_file.readline()

    if line:
        print(">> There's a line, if statement is true", repr(line))
        print_line(line, encoding, errors)
        print(">> Calling main again")
        return myencoding(language_file, encoding, errors)
    print("<<< Exit main")

def print_line(line, encoding, errors):
    #print(">>> print_line", repr(line), encoding, errors)
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # print("line: ", line)
    print(raw_bytes, "<====>", cooked_string)
    #print("<<<<< Exit print_line")

languages = open("languages.txt", encoding="utf8")

myencoding(languages, input_encoding, error)
