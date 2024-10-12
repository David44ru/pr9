def collect_odd_numbers():

    numbers = []


    while True:
        user_input = input("Введите число (или 'end' для завершения): ")
        if user_input == "end":
            break
        try:

            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Это не число. Попробуйте еще раз.")


    odd_numbers = [num for num in numbers if num % 2 != 0]


    print("Нечётные числа из списка:", odd_numbers)


while True:
    collect_odd_numbers()


    answer = input("Вы хотите продолжить? да/нет: ").lower()


    if answer != "да":
        print("Программа завершена.")
        break
