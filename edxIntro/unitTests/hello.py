def main():
    name = input("What's your name? ")
    #hello(name)
    print(hello(name))

def hello(to="world"):
    # print("hello,", to)
    return f"hello, {to}"

if __name__ == "__main__":
    main()
