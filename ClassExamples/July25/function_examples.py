

def hello():
    print("Hello, Earthling!")

def hello2():
    return "Hi!"

def hello3(name):
    print(f"Hello, {name}")

def hello4(message, *name):
    if len(name) == 0:
        name = "World"
    for n in name:
        print(f"{message}, {n}!")

def hello5(*, message, name, punctuation):
    if len(name) == 0:
        name = "World"
    for n in name:
        print(f"{message}, {n} {punctuation}")

def hello6(*, message, name, punctuation, **kwargs):
    if len(name) == 0:
        name = "World"
    for n in name:
        print(f"{message}, {n} {punctuation}")

def hello7(name, message="Greatings"):
    print(f"{message}, {name}")


hello7("Olaf")
hello7("Sven", message="Hi")
