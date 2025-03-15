k = 0
d = []
n1 = []
s0 = []

with open("base.txt", 'r+') as file:
    data = file.readlines()
    # Сохраняем исходные данные для последующего перезаписи файла
    original_data = data.copy()
    for i in data:
        s = [x for x in i.split(":")]
        if s[0] in s0:
            k += 1
            d.append(s[0])
            # Удаляем строку с повторяющимся словом
            original_data.remove(i)
        s0.append(s[0])
        if len(s)==3:
            print(s)

    # Перезаписываем файл с удаленными строками
    file.seek(0)
    file.truncate()
    file.writelines(original_data)

print(f'Количество дубликатов слов в словаре - {k}\n', d)