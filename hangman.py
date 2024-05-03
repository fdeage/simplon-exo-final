import random
from list_of_words import brit_words, french_words

def hangman(word):
    print("Welcome to Hangman!")
    print("Guess the word in less than 10 attempts")

    word = word.lower()
    word = list(word)

    display = []
    for i in range(len(word)):
        display.append("_")
    print(display)

    hangman_construct = [
        "  ____", 
        " |    |",
        " |    O",
        " |   /|\\",
        " |   / \\",
        " |",
        "_|_"
    ]

    attempts = 0
    while attempts < 10:
        print("\n")
        guess = input("Enter your guess: ")
        guess = guess.lower()
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
            print("Yes ! ", guess, "is not in the word.")
            print("\n")
            print(display)
        else:
            print("Nope ! ", guess, "is not in the word.")
            print("\n")
            print(display)
            print("\n")
            print("Here's the gallows:")
            print("\n".join(hangman_construct[:attempts + 1]))
            attempts += 1
        if "_" not in display:
            print("You win!")
            break
    if attempts == 10:
        print("You lose! The word was: ", word)


if __name__ == "__main__":
    random_word = random.choice(brit_words)

    hangman(random_word)