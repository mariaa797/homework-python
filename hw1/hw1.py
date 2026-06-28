# Дано список цілих чисел. Визначте елемент у списку з найбільшим значенням.
#  Надрукувати значення найбільшого елемента, а потім номер індексу. 
#  Якщо найбільший елемент не є унікальним, надрукуйте індекс першого входження найбільшого елемента.
# Тобто:
# Програма має очікувати від користувача (input) список чисел (так, це треба перетворити на список чисел)
# А потім повернути два числа через print


numbers_str = str(input("Enter list of numbers with spaces: ")).split()
numbers = list(map(int, numbers_str))

max_value = max(numbers)
max_value_index = numbers.index(max_value)

print(max_value, max_value_index)