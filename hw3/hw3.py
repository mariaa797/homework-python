# Напишіть програма, яка отримує значення середньомісячної кількості опадів по 
# місяцях (в мм) і повертає загальний обсяг опадів
#  протягом року, середньорічну кількість опадів, назви місяців та значення з 
#  найвищим та найменшим числом опадів протягом року. 
#  Програма має сваритися на неправильні дані: менше або більше 12 чисел, не 
#  числа або не той формат)
# Має бути 4 функції: отримання вводу користувача, перевірка ввідних даних,
# обчислення значень, вивід їх.

def get_input():
    return input("Enter mm values for each month: ").split()


def check_input(numbers_str):
    if len(numbers_str) != 12:
        print("Enter 12 values")
        exit()

    numbers = []

    for val in numbers_str:
        try:
            number = float(val)
        except ValueError:
            print("Not a number")
            exit()

        if number < 0:
            print("Negative value")
            exit()

        numbers.append(number)

    return numbers


def calculate_values(numbers):
    months = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]

    total = sum(numbers)
    annual_average = total / 12

    max_value = max(numbers)
    max_index = numbers.index(max_value)

    min_value = min(numbers)
    min_index = numbers.index(min_value)

    return (
        total,
        annual_average,
        (max_value, months[max_index]),
        (min_value, months[min_index])
    )


def print_results(result):
    print(result)


def main():
    info = get_input()
    numbers = check_input(info)
    result = calculate_values(numbers)
    print_results(result)


main() 