numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_numbers = sum(numbers[5:]) + sum(numbers[0:4])  # Cумма всех чисел в списке
len_numbers = len(numbers)  # Количество всех элементов в списке
numbers[4] = sum_numbers / len_numbers  # Замена None числом
print("Измененный список:", numbers)
