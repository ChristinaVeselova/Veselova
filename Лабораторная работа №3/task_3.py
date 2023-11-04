# TODO  Напишите функцию count_letters
def count_letters(text):
    text_ = text.lower()
    text_dict = {}
    dafault_count = 0
    for letter in text_:
        if letter.isalpha():
            text_dict[letter] = text_dict.get(letter, dafault_count) + 1

    return text_dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(text_dict):
    total_count = sum(text_dict.values())
    frequencies = {}
    for letter, count in text_dict.items():
        frequency = format(count / total_count, '.2f')
        frequencies[letter] = frequency

    return frequencies


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
count_dictionary = count_letters(main_str)
calculate_dictionary = calculate_frequency(count_dictionary)
for key, value in calculate_dictionary.items():
    print(f"{key}: {value}")
