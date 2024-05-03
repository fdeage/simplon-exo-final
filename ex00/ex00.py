MAX_ERROR_COUNT = 6

def print_ongoing_result(word, choice):
    print("tutu")

def choose_word():
    return "pendu"

def get_input_letter():
    return "t"


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
