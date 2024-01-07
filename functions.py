import pathlib
import random
from string import ascii_letters


def getWords(leng):
    with open("words.txt", "r") as file:
        old_list = file.read().splitlines()
    new_list = [word.lower() for word in old_list if len(word) == leng]
    return new_list


def get_random_word():
    wordlist = getWords(5)
    words = [
        word.upper()
        for word in wordlist
        if all(letter in ascii_letters for letter in word)
    ]
    return random.choice(words)


def game_over(word):
    print(f"The word was {word}")
