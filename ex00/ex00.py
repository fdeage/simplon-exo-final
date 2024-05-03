import os

MAX_ERROR_COUNT = 6
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def print_ongoing_result(word, found_letters):
    for c in word:
        if c in found_letters:
            print(c + ' ', end='')
        else:
            print("_ ", end='')

    print("\n")

def choose_word():
    word = input("Choose a word for the game: ").upper()

    os.system('clear')
    return word


def get_input_letter(found_letters):
    while True:
        chosen_letter = input("Give me a letter: ").upper()
        if len(chosen_letter) > 1:
            print("Too long you idiot")

        elif chosen_letter not in ALPHABET:
            print("not a letter you moron")

        elif chosen_letter in found_letters:
            print("you already gave me that you imbecile")

        else:
            break

    return chosen_letter

def check_letter(word, choice):
    return choice in word

def is_win(word, found_letters) -> bool:
    for c in word:
        if c not in found_letters:
            return False

    return True


def hangman():
    word = choose_word()
    choice = ""
    found_letters = []
    error_count = 0

    while True:
        print_ongoing_result(word, found_letters)
        choice = get_input_letter(found_letters)

        if check_letter(word, choice) == True:
            found_letters.append(choice)
        else:
            error_count += 1

        if error_count >= MAX_ERROR_COUNT:
            print("game over. The word was ", word)
            break

        elif is_win(word, found_letters):
            print("YOU WIN!!")
            break


    return None


if __name__ == "__main__":
    hangman()


    # is_game_over = False
    # while is_game_over == False:
