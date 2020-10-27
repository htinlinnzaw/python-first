# This is a sample Python script.

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

    def __init__(self):
        self.color = "orange"
        self.weight = 10

    def print_orange(self):
        print(self)
        print(self.color)
        print(self.weight)


if __name__ == '__main__':
    print_hi('PyCharm')
    # increment()
    # print_hi(a)
    # print_hi(increment_function(0))
    orange = Orange()
    # print(type(orange))
    # print(orange)
    orange.print_orange()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
