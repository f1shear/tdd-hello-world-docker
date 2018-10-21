# Python3


def hello_world():
    return "Hello World"


def greet(name):
    return "Hello %s" % name


if __name__ == '__main__':
    print(hello_world())
    name = input("Enter your name: ")
    print(greet(name))
