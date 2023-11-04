# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, separator=","):
    group_1 = str_1.split(separator)
    group_2 = str_2.split(separator)
    common_members = list(set(group_1).intersection(group_2))
    common_members.sort()

    return common_members


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(participants)
