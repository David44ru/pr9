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

def random_selection(ticket):
    return [random.choice(row) for row in ticket]


while True:

    user_numbers = user_selection(ticket)


    random_numbers = random_selection(ticket)

    matches = len(set(user_numbers) & set(random_numbers))


    print("\nВаш выбор:", user_numbers)
    print("Выбор программы:", random_numbers)
    print(f"Количество совпадений: {matches}")


    answer = input("Вы хотите сыграть еще раз? да/нет: ").lower()
    if answer != "да":
        print("Спасибо за игру!")
        break