##################################################
##                                              ##
##              Vokabeltrainer                  ##
##                                              ##
##################################################

# authors: Paula Stegmayer, Finn Wohnig, Paul Schabram
# date:  07.03.2024
# brief:   This program is a vocab-trainer. It is designed and programmed to train different languages and different topic-specific vocabulary

print("Menu:")
print("English (1)" + "\n" + "French (2)" + "\n" + "Spanish (3)" + "\n" + "Create your own vocab-list")

mode = int(input("Select a Language or create your own vocabs to continue (1 - 4): "))

language = ["English", "French", "Spanish", "No language chosen"] 
english = ["In the Kitchen", "Out in the nature", "Mechanical English", "Random Vocabs"]
french = ["Dans la cuisine", "Dans la nature", "Francais mécanique", "Vocabulaire aléatoire"]
spanish = ["En la cocina", "En la naturaleza", "Espanol mecánico", "Vocabulario aleatorio"]

menu2 = print("Language chosen: " , language[mode-1] + "\n" + "Vocab-Package 1 ()" + "\n" + "Vocab-Package 2" \
              + "\n" + "Vocab-Package 1" + "\n" + "Vocab-Package 1" + "\n" + "Vocab-Package 1")

if mode == 1:
    print(menu2)
elif mode == 2:
    print(menu2)
elif mode == 3:
    print(menu2)
elif mode == 4:
    print(menu2)
elif mode > 4:
    print("Sorry, this programm currently has only 4 modes available!")