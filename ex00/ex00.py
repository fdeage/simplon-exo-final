def print_ongoing_result(word, choice):
    print("tutu")

def choose_word():
    return "pendu"

def get_input():
    return "toto"


def hangman():
    word = choose_word()
    choice = ""

    # is_game_over = False
    # while is_game_over == False:

    while True:
        print_ongoing_result(word, choice)
        choice = get_input()
        break



    return None


if __name__ == "__main__":
    hangman()
