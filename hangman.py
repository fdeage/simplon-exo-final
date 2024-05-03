import random
import unicodedata

from list_of_words import brit_words, french_words
from guesses import correct_guess, wrong_guess

display = []

def game(word):
    print("Welcome to Hangman!")
    print("Guess the word in less than 8 attempts")

    og_word = list(word)
    process_word = word.lower() 
    process_word = (
        unicodedata.normalize("NFKD", process_word)
        .encode("ASCII", "ignore")
        .decode("utf-8")
    )
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
            correct_guess(og_word, process_word, guess, display)
        else:
            wrong_guess(guess, attempts, display)
            attempts += 1
        if "_" not in display:
            print("You win!")
            break

    if attempts == 8:
        print("You lose! The word was: ", word)

if __name__ == "__main__":
    random_word = random.choice(french_words)

    game(random_word)
