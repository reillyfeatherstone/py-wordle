import json
from random import randrange


def main():
    length = pick_length()
    word = generate_word(length)
    print(word)
    wordle(word)


def wordle(answer):
    guessed = "-" * len(answer)
    # guessed = generate_guess_dict(answer)
    guesses = []
    resolved = False
    
    while resolved == False:
        user_guess = guess(len(answer), guessed)
        guessed = check_answer(user_guess, answer, guessed)
        if user_guess == answer:
            print("Yes")
            resolved = True


def check_answer(user_guess, answer, guessed):
    if len(user_guess) > len(answer):
        print(f"Too long. Word is {len(answer)} characters.")
        return wordle(answer)
    if len(user_guess) < len(answer):
        print(f"Too short. Word is {len(answer)} characters.")
        return wordle(answer)

    if user_guess == answer:
        print("Congrats!")
        return main()
    for i in range(len(answer)):
        if user_guess[i] == answer[i]:
            guessed = correct_letter(i, user_guess[i], guessed)
    return guessed
    

def guess(length, guessed):
    return input(f"Guess the {length} letter word ({guessed}): ")


def correct_letter(i, letter, guessed):
    guessed = list(guessed)
    guessed[i] = letter
    output = "".join(guessed)
    return output
    

# Guessed (-1 = No, 0 = Yes but elsewhere, 1 = Yes)
def generate_guess_dict(word):
    guessed = {}
    counter = 1
    for letter in word:
        guessed[str(counter)] = "x"
        counter += 1
    return guessed


def pick_length():
    length = input("Pick a word length: ")
    dictionary = read_dict(length)
    if dictionary is None:
        print("No words with that length.")
        return pick_length()
    return length


def read_dict(length):
    path = "dictionary.json"
    f = open(path, 'r')
    dictionary = json.load(f)
    f.close()

    try:
        return dictionary[length]
    except:
        return None


def generate_word(word_length):
    dictionary = read_dict(word_length)
    dict_length = len(dictionary)
    key = randrange(0, dict_length + 1)
    
    return get_word_from_json(dictionary, key)


def get_word_from_json(json_data, index):
    try:
        # Access the word using the provided word length and index
        return json_data[str(index)]
    except KeyError:
        # Handle the case where the word doesn't exist
        return None


main()
