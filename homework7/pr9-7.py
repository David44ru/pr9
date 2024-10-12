def cyclic_shift_right(numbers):
    
    if numbers:  
        last_element = numbers.pop()  
        numbers.insert(0, last_element)  
    return numbers


while True:
    
    user_input = input("Введите числа через запятую: ")
    
    
    numbers = [int(num.strip()) for num in user_input.split(",")]

    
    updated_numbers = cyclic_shift_right(numbers)

    
    print("Список после циклического сдвига вправо:", updated_numbers)

    
    answer = input("Вы хотите продолжить? да/нет: ").lower()
    if answer != "да":
        print("Программа завершена.")
        break
