salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total_deficit = 0
for month in range(months):
    current_spend = spend * (1 + increase) ** month
    month_deficit = max(0, current_spend - salary)
    total_deficit += month_deficit
money_capital = round(total_deficit)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
