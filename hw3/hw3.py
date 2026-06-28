# Напишіть програма, яка отримує значення середньомісячної кількості опадів по 
# місяцях (в мм) і повертає загальний обсяг опадів
#  протягом року, середньорічну кількість опадів, назви місяців та значення з 
#  найвищим та найменшим числом опадів протягом року. 
#  Програма має сваритися на неправильні дані: менше або більше 12 чисел, не 
#  числа або не той формат)
# Має бути 4 функції: отримання вводу користувача, перевірка ввідних даних,
# обчислення значень, вивід їх.

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]


def a():
    data = input().split()

    if len(data) != 12:
        raise ValueError

    numbers = []

    for x in data:
        try:
            numbers.append(float(x))
        except:
            raise ValueError

    return numbers


def b(info):
    pass


def c(info):
    total = sum(info)
    average = total / len(info)

    max_value = max(info)
    min_value = min(info)

    max_month = months[info.index(max_value)]
    min_month = months[info.index(min_value)]

    return (
        total,
        average,
        (max_value, max_month),
        (min_value, min_month)
    )


def d(result):
    print(result)


def main():
    info = a()
    b(info)
    result = c(info)
    d(result)


main()