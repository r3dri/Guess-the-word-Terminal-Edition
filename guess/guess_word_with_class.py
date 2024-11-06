import os
import random

class Game:
    def __init__(self):
        self.health = 0
        self.guesses = [' ']
        self.wrong_guesses = []
        self.word = ""
        self.question = ""
        self.length = ""

    def txt2screen(self, x):
        os.system('clear')
        with open(f"ascii_{x}.txt", 'r+') as file:
            data = file.readlines()
            for i in data:
                print(i.replace('\n', ''))

    def randword(self):
        data = []
        with open("base.txt", 'r+') as file:
            d = file.readlines()
            for i in d:
                data.append([x for x in i.split(":")])
        word_random = random.choice(data)
        self.word = str(word_random[0]).upper()
        self.question = word_random[1]
        if ' ' in self.word:
            self.length = f'2 слова | Количество букв - {len(self.word)-1}'
        else:
            self.length = f'1 слово | Количество букв - {len(self.word)}'

    def reveal_letters(self):
        revealed_word = ""
        for letter in self.word:
            if letter in self.guesses:
                revealed_word += letter
            else:
                revealed_word += "*"
        return revealed_word

    def show_word(self):
        hidden_word = []
        for i in range(len(list(self.word))):
            if self.word[i] != ' ':
                hidden_word.append('*')
            else:
                hidden_word.append('  ')
        revealed_word = self.reveal_letters()
        return revealed_word

    def helloscreen(self):
        self.txt2screen('hello')
        print('1.Начать игру')
        print('2.Правила игры')
        print('3.Выйти')
        print('')
        vvod_main = input("Для выбора действия введите его номер(1-3):")
        if vvod_main == '1':
            self.start_game()
        elif vvod_main == '2':
            self.rules_screen()
        elif vvod_main == '3':
            os.system('clear')
            exit()
        else:
            os.system('clear')
            self.helloscreen()

    def rules_screen(self):
        self.txt2screen('rules')
        print('1.Вернуться на главную')
        print('')
        vvod_main = input("Введите 1 чтобы вернуться на главную:")
        if vvod_main == '1':
            self.helloscreen()
        else:
            os.system('clear')
            self.rules_screen()

    def start_game(self):
        os.system('clear')
        k = 0
        while k == 0:
            try:
                self.health = int(input("Введите количество жизней: "))
                k += 1
            except:
                print("Вы ввели некорректные данные.")
        self.randword()
        self.guesses = [' ']
        os.system('clear')
        while self.health > 0:
            os.system('clear')
            print(self.question)
            print(self.show_word(), f'| {self.length}')
            print(f'Оставшееся количество жизней - {self.health}.')
            print(f"Исключенные буквы: {', '.join(self.wrong_guesses)}")
            tryed = input("Введите предполагаемую букву: ")
            if len(tryed) == 1:
                if tryed.upper() in self.word:
                    self.guesses.append(tryed.upper())
                else:
                    self.health -= 1
                    self.wrong_guesses.append(tryed.upper())

            if self.show_word().count('*') == 0 or tryed.upper() == self.word:
                self.txt2screen('win')
                break
        if self.health == 0:
            print("")
            self.txt2screen('go')
        print("")
        print(f'{self.word} - {self.question}')
        print("")
        print("_______________________")
        print("1.Сыграть снова")
        print('2.Выйти')
        k = 0
        while k == 0:
            try:
                vvod_data = int(input("Для выбора действия введите его номер(1-2):"))
                k += 1
            except:
                print("")
        if vvod_data == 1:
            self.start_game()
        elif vvod_data == 2:
            os.system('clear')
            exit()
        else:
            self.helloscreen()


game = Game()
game.helloscreen()