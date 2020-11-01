import math

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

a = 0


# un-functional function
def increment():
    global a
    a += 1


# functional function
def increment_function(b):
    return b + 1


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Orange:
    print("Orange created")

    def __init__(self, weight, color):
        self.mold = 0
        self.weight = weight
        self.color = color

    def print_orange(self):
        print(self)
        print(self.color)
        print(self.weight)

    def rot(self, days, temperature):
        self.mold = days * (temperature * .1)


def print_hello_world():
    for i in range(100):
        print("Hello World")


def print_diagonal(length, width):
    d = math.sqrt(length ** 2 + width ** 2)
    print(d)


# methods surrounded on both sides by underscores are magic methods
if __name__ == '__main__':
    print_hi('PyCharm')
    # increment()
    # print_hi(a)
    # print_hi(increment_function(0))
    # orange = Orange(10, "red")
    # print(type(orange))
    # print(orange)
    # orange.print_orange()
    # print(orange.color)
    # print(orange.weight)
    # print(orange.mold)
    # orange.rot(10, 98)
    # print(orange.mold)
    # print_hello_world()
    # print_diagonal(2, 3)
    # print("""This is a really really really really really really
    # really really long line of code.""")
    x = 10
    x = x + 1  # increment
    x += 1  # increment
    x -= 1  # decrement
    # print(x)
    # var = 2 / 0
    # print(var)
    # var1 = 0
    var2 = 13 // 8  # integer division/ floor quotient
    print(var2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
