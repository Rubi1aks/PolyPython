def find_common_participants(group1, group2, delimiter=','):
    # Разделяем строки на списки участников, используя указанный разделитель
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    # Находим общих участников, сортируем результат в алфавитном порядке
    common_participants = sorted(participants1.intersection(participants2))

    return common_participants


# Пример использования функции с другим разделителем
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверка работы функции
common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')
print("Общие участники:", common_participants)
