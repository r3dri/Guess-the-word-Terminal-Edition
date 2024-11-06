print('\x1b[2J')
print('\x1b[H')
# Загрузка текста приветствия
with open("ascii_hello2.txt", 'r+') as file:
    data = file.readlines()
    for i in data:
        print(i.replace('\n', ''))

# Вывод правил игры
with open("rules.txt", 'r+') as file:
    data = file.readlines()
    for i in data:
        print(i.replace('\n', ''))

# Меню игры
print('1.Начать игру')
print('2.Выйти')
print('')
vvod_main = input("Для выбора действия введите его номер(1-2):")
print('\x1b[2J')
print('\x1b[H')
# Обработка выбора меню
if vvod_main == '1':
    m=0
    while m==0:
        # Начало игры
        k = 0
        while k == 0:  # проверка на буквы
            try:
                print('\x1b[2J')
                print('\x1b[H')
                health = int(input("Введите количество жизней: "))
                k += 1
            except:
                print('\x1b[2J')
                print('\x1b[H')
                print("Вы ввели некорректные данные.")

        # Загрузка слова из файла
        data = []
        with open("base.txt", 'r+') as file:
            d = file.readlines()
            for i in d: data.append([x for x in i.split(":")])
        # Получаем случайное число из файла /dev/urandom
        with open('/dev/urandom', 'rb') as file:
            random_bytes = file.read(1)
        # Преобразуем байт в целое число
        random_int = int.from_bytes(random_bytes, 'big')
        # Масштабируем число к диапазону [0, 1000]
        random_int %= 1001
        random=data[random_int]
        word = str(random[0]).upper()
        question = random[1]
        length = f'2 слова | Количество букв - {len(word) - 1}' if ' ' in word else f'1 слово | Количество букв - {len(word)}'
        guesses = [' ']
        wrong_guesses = []

        # Игровой цикл
        while health > 0:
            print('\x1b[2J')
            print('\x1b[H')
            print(question)
            print(f'{" ".join(["*" if letter not in guesses else letter for letter in word])} | {length}')
            if len(wrong_guesses) > 0:
                print(f'Исключенные буквы - {set(wrong_guesses)}')
            print(f'Оставшееся количество жизней - {health}.')
            tryed = input("Введите предполагаемую букву: ")
            if len(tryed) == 1 and tryed.isalpha():
                if tryed.upper() in word:
                    guesses.append(tryed.upper())
                else:
                    health -= 1
                    wrong_guesses.append(tryed)

            if "*" not in "".join(["*" if letter not in guesses else letter for letter in word]) or tryed.upper() == word:
                # Вывод текста победы
                print('\x1b[2J')
                print('\x1b[H')
                with open("ascii_win.txt", 'r+') as file:
                    data = file.readlines()
                    for i in data:
                        print(i.replace('\n', ''))
                break

        # Вывод текста проигрыша, если жизней не осталось
        if health == 0:
            print('\x1b[2J')
            print('\x1b[H')
            print("")
            with open("ascii_go.txt", 'r+') as file:
                data = file.readlines()
                for i in data:
                    print(i.replace('\n', ''))

        print("")
        print(f'{random[0]} - {random[1]}')
        print("")
        print("_______________________")
        print("1.Сыграть снова")
        print('2.Выйти')

        k = 0
        while k == 0:  # проверка на буквы
            try:
                vvod_data = int(input("Для выбора действия введите его номер(1-2):"))
                k += 1
            except:
                print("")

        if vvod_data == 2:
            print('\x1b[2J')
            print('\x1b[H')
            exit()

elif vvod_main == '2':
    # Выход из игры
    exit()
