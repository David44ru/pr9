def calculate_squares():

    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))

    if a > b:
        a, b = b, a

    squares = [x**2 for x in range(a + 1, b)]

    print("Квадраты чисел между a и b:", squares)

while True:
    calculate_squares() 
   
    answer = input("Вы хотите продолжить? да/нет: ").lower()


    if answer != "да":
        print("Программа завершена.")
        break
