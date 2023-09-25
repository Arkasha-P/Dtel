import csv

# Открываем исходный CSV файл для чтения
with open('txt/street.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Добавляем данные в определенную колонку
new_data = ['новые данные 1', 'новые данные 2', 'новые данные 3']
column_index = 4  # индекс колонки, в которую нужно добавить данные

for i in range(len(rows)):
    rows[i].insert(column_index, new_data[i])

# Открываем новый CSV файл для записи
with open('txt/street.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)