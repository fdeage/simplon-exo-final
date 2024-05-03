def print_ongoing_result(word, choice):
    print("tutu")

def choose_word():
    return "pendu"

def get_input():
    return "toto"

def check_letter():
    return True
    

def hangman():
    word = choose_word()
    choice = ""
    found_letters = []
    error_count = 0

    while True:
        print_ongoing_result(word, found_letters)  
        choice = get_input()
        result = check_letter(word, choice)
        break
        

    return None



# def score(numbre, total):
#     if pendu 
#     return total



if __name__ == "__main__":
    hangman()