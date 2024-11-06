def clear():
    print('\x1b[2J')
    print('\x1b[H')
def txt2screen(x):
    clear()
    with open(f"ascii_{x}.txt", 'r+') as file:
        data = file.readlines()
        for i in data:
            print(i.replace('\n', ''))

def randword():
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
    random = data[random_int]
    return random
def helloscreen():
    txt2screen('hello')
    print('1.Начать игру')
    print('2.Правила игры')
    print('3.Выйти')
    print('')
    vvod_main = input("Для выбора действия введите его номер(1-3):")
    if vvod_main == '1':
        start_game()
        #добавить функцию начала
    elif vvod_main == '2':
        rules_screen()
    elif vvod_main == '3':
        clear()
        exit()
    else:
        clear()
        helloscreen()

def rules_screen():
    txt2screen('rules')
    print('1.Вернуться на главную')
    print('')
    vvod_main = input("Введите 1 чтобы вернуться на главную:")
    if vvod_main == '1':
        helloscreen()
    else:
        clear()
        rules_screen()

def reveal_letters(word, guessed_letters):
    revealed_word = ""
    for letter in word:
        if letter in guessed_letters:  # Проверка, была ли буква угадана
            revealed_word += letter
        else:
            revealed_word += "*"
    return revealed_word

def show_word(x,guessed_letters):
    letters=guessed_letters
    word=list(x)
    hidden_word=[]
    for i in range(len(list(x))):
        if word[i]!=' ':
            hidden_word.append('*')
        else: hidden_word.append('  ')
    guessed_letters = guessed_letters  # список куда вносятся угаданные символы
    revealed_word = reveal_letters(word, guessed_letters)
    return revealed_word

def start_game():
    clear()
    k = 0
    while k == 0:  # проверка на буквы
        try:
            health = int(input("Введите количество жизней: "))
            k += 1
        except:
            print("Вы ввели некорректные данные.")
    random=randword()
    word=str(random[0]).upper()
    question=random[1]
    if ' ' in word:
        length = f'2 слова | Количество букв - {len(word)-1}'
    else:
        length = f'1 слово | Количество букв - {len(word)}'
    guesses=[' ']
    wrong_guesses=[]
    clear()
    while health>0:
        clear()
        print(question)
        print(show_word(word, guesses),f'| {length} ')
        if len(wrong_guesses)>0:
            print(f'Исключенные буквы - {set(wrong_guesses)}')
        print(f'Оставшееся количество жизней - {health}.')
        tryed = input("Введите предполагаемую букву: ")
        if len(tryed)==1 and tryed.isalpha():
            if tryed.upper() in word:
                guesses.append(tryed.upper())
            else:
                health-=1
                wrong_guesses.append(tryed)
        if show_word(word, guesses).count('*')==0 or tryed.upper()==word:
            txt2screen('win')
            break
        if len(tryed)>1 and tryed.upper()!=word:
            health-=1
    if health==0:
        print("")
        txt2screen('go')
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
    if vvod_data == 1:
        start_game()
    elif vvod_data == 2:
        clear()
        exit()
    else:
        helloscreen()

helloscreen()