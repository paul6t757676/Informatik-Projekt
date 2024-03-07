##################################################
##                                              ##
##              Vokabeltrainer                  ##
##                                              ##
##################################################

# authors: Paula Stegmayer, Finn Wohnig, Paul Schabram
# date:  07.03.2024
# brief:   This program is a vocab-trainer. It is designed and programmed to train different languages and different topic-specific vocabulary

print("Menu:")
print("English (1)" + "\n" + "French (2)" + "\n" + "Spanish (3)" + "\n" + "Create your own vocab-list (4)" + "\n" + "Help (5)")

mode = int(input("Select a Language or create your own vocabs to continue (1 - 4). Enter '9' to get help: "))
help = print("Help needed? This program is a vocabulary-trainer....(hier mehr Hilfe-Text noch einfügen ;)")


language = ["English", "French", "Spanish", "No language chosen", help] 
english = ["Kitchen: In the Kitchen (1)", "Nature: Out in the nature (2)", "Engineering: Mechanical English (3)", "Random: Random Vocabs (4)"]
french = ["Kitchen: Dans la cuisine (1)", "Nature: Dans la nature (2)", "Engineering: Francais mécanique (3)", "Random: Vocabulaire aléatoire (4)"]
spanish = ["Kitchen: En la cocina (1)", "Nature: En la naturaleza (2)", "Engineering: Espanol mecánico (3)", "Random: Vocabulario aleatorio (4)"]
modetranslation = [english, french, spanish]


menu2 = print("Language chosen: " + language[mode-1]), print(modetranslation[mode-1])
chosen_program = int(input("Choose one specific vocab-unit you'd like to train (1 - 4): "))
if mode == 5:
    help
else:
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
    elif mode > 5:
        print("Sorry, this programm currently has only 4 modes available!")