import json

FILENAME = "input.json"  # Укажите имя вашего JSON файла


def task() -> float:
    total_sum = 0.0

    # Читаем данные из JSON файла
    with open(FILENAME, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        # Проходим по каждому словарю в списке
        for item in data:
            # Извлекаем значения и вычисляем произведение
            score = item.get("score", 0)  # Если ключа нет, использовать 0
            weight = item.get("weight", 0)  # Если ключа нет, использовать 0

            #print(f"Произведение {score} * {weight} = {weight*score}")  # Отладочный вывод

            total_sum += score * weight

    return round(total_sum, 3)  # Округляем до 3 знаков после запятой


if __name__ == '__main__':
    result = task()
    print(result)
