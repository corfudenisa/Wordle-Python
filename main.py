from functions import processWord, get_random_word, game_over, refresh_page

word = get_random_word()

for guess_num in range(1, 7):
    guess = input(f"\nGuess {guess_num}: ")
    while processWord(guess, word):
        _ = _
    if guess == word:
        print("GOOD JOB!\n")
        break
    else:
        game_over()
