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

def correct_guess(og_word, process_word, guess, display):
    for i in range(len(process_word)):
        if process_word[i] == guess:
            display[i] = og_word[i]
    print("Yes ! ", guess, "is in the word.")
    print("\n")
    print(display)

def wrong_guess(guess, attempts, display):
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