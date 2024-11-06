import random

def create_hidden_word(word):
    """Создает строку с символами "_" вместо букв в слове.

    Args:
        word: Слово, которое нужно скрыть.

    Returns:
        Строка с "_" вместо букв в слове.
    """

    hidden_word = "_" * len(word)  # Создает строку с символами "_" длиной слова
    return hidden_word

def reveal_letters(word, hidden_word, guessed_letters):
    revealed_word = ""
    for letter in word:
        if letter in guessed_letters:  # Проверка, была ли буква угадана
            revealed_word += letter
        else:
            revealed_word += "_"
    return revealed_word


# Пример использования:
word = "python"  # Слово, которое нужно скрыть
hidden_word = create_hidden_word(word)
guessed_letters = ["p", "t", "h"] # Угаданные буквы
revealed_word = reveal_letters(word, hidden_word, guessed_letters)

print(f"Слово: {revealed_word}")  # Вывод: Слово: p_th_n
print('hello world')
