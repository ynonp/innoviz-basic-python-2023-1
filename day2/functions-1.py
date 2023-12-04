def say_hi():
    """
    this function prints some text to the screen
    :return: nothing
    """
    print("one")
    print("two")
    print("three")


def twice(x: int) -> int:
    """
    takes a number and returns it multiplied by 2
    :param x:
    :return:
    """
    return x * 2


def apply(f, x):
    return f(x)


print(apply(twice, 8))


print(twice(10))
num = input("pick a number: ")
print(twice(num))

