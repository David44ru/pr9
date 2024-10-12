import random

ticket = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
]

def user_selection(ticket):
    user_numbers = []
    for row in ticket:
        while True:
            try:
                number = int(input(f"Выберите число из ряда {row}: "))
                if number in row:
                    user_numbers.append(number)
                    break
                else:
                    print("Число должно быть из указанного ряда. Попробуйте еще раз.")
            except ValueError:
                print("Пожалуйста, введите правильное число.")
    return user_numbers