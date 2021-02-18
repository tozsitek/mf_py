# input validation

# encapsulating it all in one function
def get_not_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I did not understand that.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value


def sanitised_input_mf(prompt, type=None, min=None, range=None):
    if min is not None and max is not None and max < min:
        raise ValueError("min must be less than or equal to max.")
    while True:
        ui = input(prompt)
        if type is not None:
            try:
                ui = type(ui)
            except ValueError:
                print("Input type must be 0.")

def sanitised_input(prompt, type_=None, min_=None, max_=None, range_=None):
    if min_ is not None and max_ is not None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and ui > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and ui < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        elif range_ is not None and ui not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    expected = " or ".join((
                        ", ".join(str(x) for x in range_[:-1]),
                        str(range_[-1])
                    ))
                    print(template.format(expected))
        else:
            return ui



#age = get_not_negative_int("Please enter your age: ")
#kids = get_not_negative_int("Please enter the number of children you have: ")
#salary = get_not_negative_int("Please enter your early earnings, in dollars: ")

age = sanitised_input("Enter your age: ", int, 1, 101)
answer = sanitised_input("Enter your answer: ", str.lower, range_=('a', 'b', 'c', 'd'))

#data = input("Please enter something in all CAPs: ")
#while not data.isupper():
#    print("Sorry, your entry is not all upppercase letters.")
#    data = input("Please enter an all upper case string: ")
