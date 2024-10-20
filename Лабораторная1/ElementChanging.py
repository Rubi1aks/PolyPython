numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

sum_of_numbers = sum(num for num in numbers if num is not None)
count_of_numbers = len(numbers)

average = round(sum_of_numbers / (count_of_numbers), 2)

numbers = [average if num is None else num for num in numbers]

print("Измененный список:", numbers)
