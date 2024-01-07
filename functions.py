import pathlib
import random
from string import ascii_letters


def getWords(leng):
    with open("words.txt", "r") as file:
        old_list = file.read().splitlines()
    new_list = [word.lower() for word in old_list if len(word) == leng]
    return new_list
def checkWord(word) -> bool:
    if(len(list(word))!=5):
        print("YOUR WORD MUST HAVE 5 LETTERS")
        return False
    Letters=[let for let in word]
    ASCII_LETTERS = {chr(i): i for i in range(ord('A'), ord('Z')+1)}
    for let in Letters:
        if let not in ASCII_LETTERS:
            print(f"{let} IS NOT ALLOWED")
            return False
    return True


def get_random_word():#Denisa
    return 0
def processWord(word):
    #word = get_random_word()
    randWord = "SNAKE"
    word = word.upper
    if checkWord(word):
        print("Good")
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

