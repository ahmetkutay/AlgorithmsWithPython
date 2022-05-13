# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(a, b):
    if b != 0:
        t = a
        a = b
        b = t % b
        return b
    return a

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(print_hi(60, 96))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
