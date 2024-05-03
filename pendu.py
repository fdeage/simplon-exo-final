import getpass

# demande un mot a deviner 
# def ask_word (): return input("taper un mot : " )
def ask_word (): return getpass.getpass("taper un mot : " )


# check existance du mot 
def not_valid_word (secret,dico): return True if secret not in dico else False

# etape de recuperation d'un choix valide de mot
def get_valid_word (word):
    while (not_valid_word(word)):
        letter=ask_word()
    return letter 


# demande une lettre
def ask_letter (): return input("taper une lettre: ",)[0]

# check valid letter 
def not_valid_letter (letter) : return True if not letter.isalpha() else False

# etape de recuperation d'un choix valide de lettre
def get_valid_letter ():
    letter=ask_letter()
    while (not_valid_letter(letter)):
        letter=ask_letter()
    return letter 

# determine lres points de vie 
def get_life(word) : return min(3,len(word))
    
# check lettre is in word
def letter_in_word (word,letter): return True if letter in word else False 

# enleve les lettre trouvé 
def maj (to_find_letter,letter): 
    
    try :
        while True : 
            cible=to_find_letter.index(letter)
            del(to_find_letter[cible])
    except : 
        return to_find_letter

def show_progression (word,to_find_letter):
    view = ""
    for l in word :
        if l in to_find_letter : 
            view+="_"
        else : 
            view+=l

    print (view)

#  main  : 
def main (verif=False):

    print("""
     __                   .___                                .___     
    |__| ____  __ __    __| _/_ __  ______   ____   ____    __| _/_ __ 
    |  |/ __ \|  |  \  / __ |  |  \ \____ \_/ __ \ /    \  / __ |  |  \ 
    |  \  ___/|  |  / / /_/ |  |  / |  |_> >  ___/|   |  \/ /_/ |  |  /
/\__|  |\___  >____/  \____ |____/  |   __/ \___  >___|  /\____ |____/ 
\______|    \/             \/       |__|        \/     \/      \/      
""")

    not_end=True
    
    # life=get_life()

    word=ask_word()
    if verif ==True : word=get_valid_word(word)

    word=word.lower()

    life=get_life(word)

    to_find_letter=list(word)

    while (not_end):
        # recup une lettre 
        letter=get_valid_letter().lower()

        # check si elle fait partis des lettres a trouver
        if letter_in_word (word,letter) :
            # si oui supprimer les lettre a trouver 
            maj (to_find_letter,letter)
        else : life-=1

        show_progression (word,to_find_letter)
        print("vie restante: ",life*"<3 ")

        if len(to_find_letter)==0 or life==0 : not_end=False

    
    if life==0 :
        print("you loose , that was ",word)

    else : 
        print("you win")
        
    return 0
    

if __name__== "__main__" :
    main()
        
        

