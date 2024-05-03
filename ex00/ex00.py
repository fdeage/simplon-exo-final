MAX_ERROR_COUNT = 6
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def print_ongoing_result(word, choice):
    print("tutu")

def choose_word():
    return "pendu"

def get_input_letter(found_letters):
    while True:
        chosen_letter = input("Give me a letter: ").upper()
        if len(chosen_letter) > 1:
            print("Too long you idiot")

        elif chosen_letter not in ALPHABET:
            print("not a letter you moron")

        elif chosen_letter in found_letters
            print("you already gave me that you imbecile")

        else:
            break

    return chosen_letter


def check_letter(word, choice):
    return True

def hangman():
    word = choose_word()
    choice = ""
    found_letters = []
    error_count = 0

    while True:
        print_ongoing_result(word, found_letters)
        choice = get_input_letter()
        result = check_letter(word, choice)

        if result == True:
            found_letters.append(choice)
        else:
            error_count += 1

            if error_count >= MAX_ERROR_COUNT:
                print("game over. The word was ", word)
                break

        print(found_letters)

    return None


if __name__ == "__main__":
    hangman()


    # is_game_over = False
    # while is_game_over == False:
