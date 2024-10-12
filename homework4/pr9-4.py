def count_even_odd_numbers():

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

    even_count = len([num for num in numbers if num % 2 == 0])
    odd_count = len([num for num in numbers if num % 2 != 0])

    
    print(f"Количество чётных чисел: {even_count}")
    print(f"Количество нечётных чисел: {odd_count}")


while True:
    count_even_odd_numbers() 

    
    answer = input("Вы хотите продолжить? да/нет: ").lower()

   
    if answer != "да":
        print("Программа завершена.")
        break
