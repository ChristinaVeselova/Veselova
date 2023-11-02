money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

count = 0  # Количество месяцев, которое можно протянуть без долгов
current_money = salary + money_capital  # Бюджет текущего месяца
while spend <= current_money:
    count += 1
    spend += count * increase * spend
    if spend > current_money:
        break
print("Количество месяцев, которое можно протянуть без долгов:", count)
