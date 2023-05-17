from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Marianna") == "hello, Marianna"

def test_multiple():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"
        


