from config import MAX_ERROR_COUNT

def print_ongoing_result(word, found_letters, error_count):
    for c in word:
        if c in found_letters:
            print(c + " ", end="")
        else:
            print("_ ", end="")

    print_score(error_count)


def print_score(error_count):
    print("                  - Errors: ", error_count, "/", MAX_ERROR_COUNT, "\n")
