##################################################
##                                              ##
##              Vokabeltrainer                  ##
##                                              ##
##################################################

# authors: Paula Stegmayer, Finn Wohnig, Paul Schabram
# date:  07.03.2024
# brief:   This program is a vocab-trainer. It is designed and programmed to train different languages and different topic-specific vocabulary

### selection-menu: The preferred language, creating an own vocab list or a help function can be chosen here ###
import os
def selection_menu():
    while True:
        print("\nMenu:")
        print("(1) English" + "\n" + "(2) French" + "\n" + "(3) Spanish" + "\n" + "(4) Create your own vocab-list" + "\n" + "(5) Help" + "\n")    
                           #print options
        try:
            mode = int(input("Select a Language or create your own vocabs to continue (1 - 4). Enter '5' to get help: "))  
            os.system('cls' if os.name == 'nt' else 'clear')                                         #select chosen option 
            help = "\nHelp needed? This program is a vocabulary-trainer. It can support you improving your language skills by asking you for the correct\
                translation of different vocabs. There are different languages and modes you can select. You can either improve your english, spanish,\
                or your french skills, or as an extra option you can create your own vocab list, which will be used for your vocab training.\n-----------------------"
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
        except:
                print("Invalid input! Please choose a correct Number for the Programm\n")

### vocabset_menu: one of the available vocab lists can be chosen ###
def vocabset_menu(mode):
    language = ["English", "French", "Spanish", "No language chosen", help] 
    menu2 = print("Language chosen: " , (language[mode-1]),"\n-----------------------\nPossible Topics:\n")
    english = ["Kitchen: In the Kitchen (1)", "Nature: Out in the nature (2)", "Engineering: Mechanical English (3)", "Random: Random Vocabs (4)"]
    french = ["Kitchen: Dans la cuisine (1)", "Nature: Dans la nature (2)", "Engineering: Francais mécanique (3)", "Random: Vocabulaire aléatoire (4)"]
    spanish = ["Kitchen: En la cocina (1)", "Nature: En la naturaleza (2)", "Engineering: Espanol mecánico (3)", "Random: Vocabulario aleatorio (4)"]
    modetranslation = [english, french, spanish]

    while True:
        menu2 =  (print(modetranslation[mode-1]))
        chosen_program = int(input("-----------------------\nChoose one specific vocab-unit you'd like to train (1 - 4): "))
        try:
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
        except:
            print("Invalid input! Please choose a correct Number for the Programm\n")
            

### vocabset_create: an own vocab list can be created here ###
def vocabset_create():
    term = []
    definition = []
    x = 0
    while x == 0:
        newword = input("Fachbegriff: ")        # New technical term is asked
        term.append(newword)                    # New technical term is saved in  list
        newdef = input("Definition: ")          # New definition is asked
        definition.append(newdef)               # New definition is saved in list
        x = continuing_create()
        
### continuing create: Checks if another Vocab shall be added or the mode shall be closed ###
def continuing_create():
    continuing = input("Möchtest du ein weiteres Wort hinzufügen? (Y/N): ")
    if continuing == "Y":
        return 0
    elif continuing == "N":
        return 1
    else:
        return continuing_create()

# "main-Funktion": Ablaufplan des Programms mit den Funktionen in der richtigen Reihenfolge
selection_menu()