salary = 5000           # Ежемесячная зарплата
spend = 6000            # Траты за первый месяц
months = 10             # Количество месяцев, которое нужно покрыть
increase = 0.03         # Ежемесячный рост цен

# Инициализируем необходимую подушку безопасности
money_capital = 0

for _ in range(months):
    # Определяем дефицит после использования зарплаты
    deficit = max(0, spend - salary)
    money_capital += deficit
    # Увеличиваем расходы на 3% для следующего месяца
    spend *= (1 + increase)

# Округляем до целого числа
money_capital = round(money_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)

