import sys, os
from spello.model import SpellCorrectionModel
from customLemmatizer import CustomLemmatizer
from color import Color as color


def by_levenshtein_distance(lemmatizer):
    print('\n')
    print(color.BOLD + color.bluebg + "___by levenshtein distance___" + color.ENDC)
    if len(sys.argv) > 1:
        incorrect_word = sys.argv[1]
        guess_word = lemmatizer.guess_word(incorrect_word)
        print(f"Incorrect word: {incorrect_word}\nGuessed word: {guess_word}")

    while True:
        incorrect_word = input("enter the word: ")
        if incorrect_word == "q":
            exit(0)
        guess_word = lemmatizer.guess_word(incorrect_word)
        print(f"\tIncorrect word: {incorrect_word}\n\tGuessed word: {guess_word}")


def by_spello(sp):
    print('\n')
    print(color.BOLD + color.bluebg + "___by spello package___" + color.ENDC)
    if len(sys.argv) > 1:
        incorrect_word = sys.argv[1]
        guess_word = sp.spell_correct(incorrect_word)
        print(f"Incorrect word: {incorrect_word}\nGuessed word: {guess_word.get('spell_corrected_text')}")

    while True:
        incorrect_word = input("enter the word: ")
        if incorrect_word == "q":
            exit(0)
        guess_word = sp.spell_correct(incorrect_word)
        print(f"\tIncorrect word: {incorrect_word}\n\tGuessed word: {guess_word.get('spell_corrected_text')}")


if __name__ == '__main__':
    print(color.BOLD + color.blue + "\n___incorrect_word_lemmatizer___(q for exit)\n" + color.ENDC)
    choice = int(input("Which technique would you prefer:\n\t1. Levenshtein distance\n\t2. Spello package"
                       "\nenter the number of choice: "))
    if choice == 1:
        lemmatizer = CustomLemmatizer()
        by_levenshtein_distance(lemmatizer)
    else:
        print(color.UNDERLINE + "\n\twait a sec for loading a model..\t" + color.ENDC)
        sp = SpellCorrectionModel(language='en')
        os.chdir('..')
        sp.load(os.getcwd() + '//en.pkl')
        by_spello(sp)
