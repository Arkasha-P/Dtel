import sys

# Получаем аргументы командной строки, пропустив первый аргумент (имя файла)
args = sys.argv[1:]

# Проверяем, сколько аргументов было передано
if len(args) >= 3:
    # Получаем значения из аргументов
    arg1 = int(args[0])
    arg2 = int(args[1])
    arg3 = int(args[2])

    print('Первый аргумент:', arg1)
    print('Второй аргумент:', arg2)
    print('Третий аргумент:', arg3)

    # Здесь можно выполнить соответствующие действия с полученными аргументами
else:
    print('Необходимо передать три аргумента')



import argparse

# Создаем экземпляр парсера аргументов
parser = argparse.ArgumentParser()

# Добавляем ключи, которые ожидаем получить, с помощью метода add_argument()
parser.add_argument('-mass', type=int, help='Описание аргумента -mass')
parser.add_argument('-strong', type=int, help='Описание аргумента -strong')
parser.add_argument('-power', type=int, help='Описание аргумента -power')

# Разбираем аргументы командной строки
args = parser.parse_args()

# Проверяем, какие аргументы были указаны
if args.mass:
    print('Аргумент -mass был указан со значением:', args.mass)
    # Здесь можно выполнить соответствующие действия для аргумента -mass

if args.strong:
    print('Аргумент -strong был указан со значением:', args.strong)
    # Здесь можно выполнить соответствующие действия для аргумента -strong

if args.power:
    print('Аргумент -power был указан со значением:', args.power)
    # Здесь можно выполнить соответствующие действия для аргумента -power