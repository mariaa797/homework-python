def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


def positive_only(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0:
                raise ValueError("Усі позиційні аргументи повинні бути додатними")
        return func(*args, **kwargs)
    return wrapper


@positive_only
def add_two(x):
    return x + 2


@shout
def add_suffix(value):
    return value + "suffix"


# Приклади
print(add_two(5))          # 7

try:
    print(add_two(-1))
except ValueError as e:
    print(e)

print(add_suffix("i"))     # ISUFFIX