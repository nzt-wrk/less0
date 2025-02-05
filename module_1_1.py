# Индексация строк

# string[начальный_символ_строки : конечный_символ_строки : шаг_между_символами_строки]

example='Стюардесса'
print(example[0])      # 0 выводит первый символ строки (нумерация с 0)
print(example[-2])     # -1 выводит последний  символ строки
print(example[4:])     # выводит все символы строки до последнего включительно с указаного 4 (нумерация с 0)
print(example[4:-1])   # выводит все символы строки с указаного(4) до конца не включая последнйи символ(-1)
print(example[::-1])   # выводит реверсивно  строку
print(example[1::2])   # выводит все символы строки до конца начиная с указанного 1(вывод со 2-го симовла т.к. нуменрация с 0) с шагом 2
print(example[1:-1:2]) # выводит все символы строки исключая последний с указанного 1(вывод со 2-го симовла т.к. нуменрация с 0) с шагом 2
print()

example='Топинамбур'
print(example[0])
print(example[-2])
print(example[4:])
print(example[::-1])
print(example[1:-1:2])