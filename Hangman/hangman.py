import random
import string


def words(words):
    words = ['chair', 'table', 'good', 'about', 'somewhere', 'go', 'fantastic', 'superb', 'church', 'asssemble', 'hug',
             'opportunity']
    while True:
        the_word = random.choice(words)
        return the_word


def hangman():
    the_word = words(words)
    word_letters = set(the_word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(the_word) > 0 and lives > 0:
        print('letters used: ', ''.join(used_letters))
        word_list = [letter if letter in used_letters else '_' for letter in the_word]
        print('current word: ', ''.join(word_list))
        user_input = ('Type a letter: ').upper()

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives -= 1
        elif user_input in used_letters:
            print('Character has already been used')
        else:
            print('Invalid character')
    if lives == 0:
        print('You run out of life')


hangman()