def getWords(leng):
    with open('words.txt', 'r') as file:
        old_list = file.read().splitlines()
    new_list = [word.lower() for word in old_list if len(word) == leng]
    return new_list

