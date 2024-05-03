import random
from list_of_words import brit_words, french_words
import random
from list_of_words import brit_words, french_words
import unicodedata

display = []

hangman_construct = [
        "  ____", 
        " |    |",
        " |    O",
        " |   /|\\",
        " |   / \\",
        " |",
        " |",
        "_|_"
    ]

def correct_guess(og_word, process_word, guess):
    for i in range(len(process_word)):
        if process_word[i] == guess:
            display[i] = og_word[i]
    print("Yes ! ", guess, "is in the word.")
    print("\n")
    print(display)

def wrong_guess(guess, attempts):
    print("Nope ! ", guess, "is not in the word.")
    print("\n")
    print(display)
    print("\n")
    print("Here's the gallows:")
    hangman=[]
    for x in range(attempts+1): 
        hangman.insert(0,hangman_construct[::-1][x])
    for x in hangman:
        print(x)

def game(word):
    print("Welcome to Hangman!")
    print("Guess the word in less than 10 attempts")

    og_word = list(word)
    process_word = word.lower()
    process_word = unicodedata.normalize('NFKD', process_word).encode('ASCII', 'ignore').decode('utf-8')
    process_word = list(process_word)

    for i in range(len(word)):
        display.append("_")
    print(display)

    attempts = 0

    while attempts < 8:
        print("\n")
        guess = input("Enter your guess: ")
        guess = guess.lower()
        if guess in process_word:
            correct_guess(og_word, process_word, guess)
        else:
            wrong_guess(guess, attempts)
            attempts += 1
        if "_" not in display:
            print("You win!")
            break

    if attempts == 8:
        print("You lose! The word was: ", word)


if __name__ == "__main__":
    random_word = random.choice(french_words)

    game(random_word)