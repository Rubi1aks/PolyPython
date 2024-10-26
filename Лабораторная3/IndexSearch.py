def find_item_index(items_list, item):
    # Проверяем, есть ли товар в списке, если да — возвращаем индекс первого вхождения
    if item in items_list:
        return items_list.index(item)
    return None

# Пример использования функции
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # Вызов функции для поиска индекса
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
