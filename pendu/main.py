MAX_ERROR_COUNT = 6

def choose_word():
    return "pendu"

def print_ongoing_result(word_to_guess, found_letters):
    return "tutu"

def get_input_letter(found_letters):
    print("Give me a letter")
    chosen_letter=input()
    while chosen_letter in found_letters == True:
        print("your letter has already been choosen")
        print("Give me another letter")
        chosen_letter=input()
    else:
        return chosen_letter

def check_letter(word_to_guess, choice):
    if choice in word_to_guess:
        print("bravo your letter is in the word")
        return True            
    else :
        print ("your letter is not in the word")
        return False      

def hangman():

    word_to_guess = choose_word()
    choice = ""
    found_letters = []
    error_count = 0
   
   
    # while is_game_over = False

    while True :
        print_ongoing_result(word_to_guess, found_letters)
        choice = get_input_letter(found_letters)
        result = check_letter(word_to_guess, choice)
        if result == True:
            print(found_letters)
            found_letters += choice
            print(found_letters)
        else:
            error_count += 1

            if error_count >= MAX_ERROR_COUNT:
                print("GAME OVER :-( the word to find was :", word_to_guess)
                break

    return None

if __name__ == "__main__":
    hangman()

    #is_game_over = False
    #while is_game_over = False