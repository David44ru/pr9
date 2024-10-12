def swap_min_max(numbers):
    # Находим минимальное и максимальное значение
    min_value = min(numbers)
    max_value = max(numbers)

    # Ищем индексы первого вхождения минимального и максимального значений
    min_index = numbers.index(min_value)
    max_index = numbers.index(max_value)

    # Меняем местами элементы
    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

    return numbers

# Цикл для повтора программы
while True:
    # Вводим список чисел через запятую
    user_input = input("Введите числа через запятую: ")
    
    # Преобразуем ввод в список чисел
    numbers = [int(num.strip()) for num in user_input.split(",")]

    # Меняем местами минимальное и максимальное значения
    updated_numbers = swap_min_max(numbers)

    # Вывод результата
    print("Список после замены:", updated_numbers)

    # Спрашиваем у пользователя, хочет ли он продолжить
    answer = input("Вы хотите продолжить? да/нет: ").lower()
    if answer != "да":
        print("Программа завершена.")
        break

