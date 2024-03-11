##################################################
##                                              ##
##              Vokabeltrainer                  ##
##                                              ##
##################################################

# authors: Paula Stegmayer, Finn Wohnig, Paul Schabram
# date:  07.03.2024
# brief:   This program is a vocab-trainer. It is designed and programmed to train different languages and different topic-specific vocabulary

### selection-menu: The preferred language, creating an own vocab list or a help function can be chosen here ###
def selection_menu():
    print("Menu:")
    print("(1) English" + "\n" + "(2) French" + "\n" + "(3) Spanish" + "\n" + "(4) Create your own vocab-list" + "\n" + "(5) Help")                         #print options

    mode = int(input("Select a Language or create your own vocabs to continue (1 - 4). Enter '5' to get help: "))                                           #select chosen option
    help = "Help needed? This program is a vocabulary-trainer....(hier mehr Hilfe-Text noch einfügen ;)"
    if mode == 5:
        print(help)
        selection_menu()
    elif mode<4:
        vocabset_menu(mode)
    elif mode == 4:
        vocabset_create()
    else:
        print("Please choose another option!")
        selection_menu()

### vocabset_menu: one of the available vocab lists can be chosen ###
def vocabset_menu(mode):
    language = ["English", "French", "Spanish", "No language chosen", help] 
    english = ["Kitchen: In the Kitchen (1)", "Nature: Out in the nature (2)", "Engineering: Mechanical English (3)", "Random: Random Vocabs (4)"]
    french = ["Kitchen: Dans la cuisine (1)", "Nature: Dans la nature (2)", "Engineering: Francais mécanique (3)", "Random: Vocabulaire aléatoire (4)"]
    spanish = ["Kitchen: En la cocina (1)", "Nature: En la naturaleza (2)", "Engineering: Espanol mecánico (3)", "Random: Vocabulario aleatorio (4)"]
    modetranslation = [english, french, spanish]


    menu2 = print("Language chosen: " , (language[mode-1]), (print(modetranslation[mode-1])))
    chosen_program = int(input("Choose one specific vocab-unit you'd like to train (1 - 4): "))

    if mode == 1:
        print(menu2)
        chosen_program
    elif mode == 2:
        print(menu2)
        chosen_program
    elif mode == 3:
        print(menu2)
        chosen_program
    elif mode == 4:
        print(menu2)
        chosen_program
    elif mode == 5:
        help
    else:
        print("Sorry, this programm currently has only 4 modes available!")


### vocabset_create: an own vocab list can be created here ###
def vocabset_create():
    own_list = []
    x = 0
    while x == 0:
        newword = input()


# "main-Funktion": Ablaufplan des Programms mit den Funktionen in der richtigen Reihenfolge
selection_menu()