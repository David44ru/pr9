import random

def find_greater_than_previous(numbers):

    result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]
    return result

while True:

    numbers = [random.randint(1, 20) for _ in range(10)]  
    print("Сгенерированный список чисел:", numbers)

    greater_elements = find_greater_than_previous(numbers)

    print("Элементы, которые больше предыдущего:", greater_elements)

    answer = input("Вы хотите продолжить? да/нет: ").lower()
    if answer != "да":
        print("Программа завершена.")
        break
