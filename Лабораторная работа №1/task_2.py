list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
middle = len(list_players) // 2  # Нахождение середины списка игроков
one_team = list_players[:middle]  # Отделение правой части от списка игроков
two_team = list_players[middle:]  # Отделение левой части от списка игроков
print(one_team)
print(two_team)
