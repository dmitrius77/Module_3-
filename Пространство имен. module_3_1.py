calls = 0                                                # Создать переменную вне функций

def count_calls():
    global calls                                         # указываем, что используем глобальное имя
    calls += 1                                           # Создан счетчик

def string_info(string):                                 # создали функцию с строкой внутри
    count_calls()                                        # обратились к функции, т.е. посчитали
    return [len(string), string.upper(), string.lower()] # вернуть длину строки, строку в верхнем регистре, строку в нижнем регистре

def is_contains(string, list_to_search):                 # создали функцию с строкой и списком
    count_calls()                                        # обратились к функции, т.е. посчитали
    string = string.lower()                              # строку выдать в нижнем регистре
    for i in list_to_search:                             # если элемент i есть в списке
        if i.lower() == string:                          # то элемент в нижнем регистре равен строке (и есть строка)
            return True                                  # вернуть true
    else:                                                # в остальных случаях
        return False                                     # вернуть false


print(string_info('Connor'))
print(string_info('Fedor'))
#print(string_info('Fedor'))
#print(string_info('Dmitrius'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)

 #НА МОЙ ВЗГЛЯД СЧЕТЧИК РАБОТАЕТ НЕ КОРРЕКТНО

