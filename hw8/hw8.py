# Завдання 1. Декоратор з *args


def log_args(func):
    def wrapper(*args, **kwargs):
        print("Arguments:", args)
        print("Keyword arguments:", kwargs)
        return func(*args, **kwargs)
    return wrapper


@log_args
def add(a, b):
    return a + b


print(add(5, 7))


# Завдання 2. Decorator factory — repeat(times)

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def hello():
    print("Привіт!")


hello()


# Завдання 3. Walrus-оператор   

words = ["cat", "house", "apple", "sun", "computer"]

for word in words:
    if (length := len(word)) > 4:
        print(word, "-", length)


# Завдання 4. Простий генератор (yield)

def countdown(n):
    while n > 0:
        yield n
        n -= 1
    yield "Старт!"


for item in countdown(5):
    print(item)