##################################################
##                                              ##
##              Vokabeltrainer                  ##
##                                              ##
##################################################

# authors: Paula Stegmayer, Finn Wohnig, Paul Schabram
# date:  07.03.2024
# brief:   This program is a vocab-trainer. It is designed and programmed to train different languages and different topic-specific vocabulary

### selection-menu: The preferred language, creating an own vocab list or a help function can be chosen here ###
### imported os library, the os library is used to have an easy way to clear the console when heading to another menu (found on stackoverflow.com)
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
                empty_lists()
            else:
                print("There are currently only 4 language-modes available. Please choose another option!")
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
        if mode == 1:
            print("Kitchen: In the Kitchen (1)" + "\n" + "Nature: Out in the nature (2)" + "\n" + "Engineering: Mechanical English (3)" + "\n" + "Random: Random Vocabs (4)" + "\n")
        elif mode==2:
            print("Kitchen: Dans la cuisine (1)" + "\n" + "Nature: Dans la nature (2)" + "\n" + "Engineering: Francais mécanique (3)" + "\n" + "Random: Vocabulaire aléatoire (4)" + "\n")
        elif mode==3:
            print("Kitchen: En la cocina (1)" + "\n" + "Nature: En la naturaleza (2)" + "\n" + "Engineering: Espanol mecánico (3)" + "\n" + "Random: Vocabulario aleatorio (4)" + "\n")
        elif mode==4:
            selection_menu()
        #menu2 =  (print(modetranslation[mode-1]))
        chosen_program = int(input("-----------------------\nChoose one specific vocab-unit you'd like to train (1 - 4): " + "\n"))
        
        # try:
        #     if mode == 1:
        #         print("Kitchen: In the Kitchen (1)" + "\n" + "Nature: Out in the nature (2)" + "\n" + "Engineering: Mechanical English (3)" + "\n" + "Random: Random Vocabs (4)" + "\n")
        #         chosen_program
        #     elif mode == 2:
        #         print("Kitchen: Dans la cuisine (1)" + "\n" + "Nature: Dans la nature (2)" + "\n" + "Engineering: Francais mécanique (3)" + "\n" + "Random: Vocabulaire aléatoire (4)" + "\n")
        #         chosen_program
        #     elif mode == 3:
        #         print("Kitchen: En la cocina (1)" + "\n" + "Nature: En la naturaleza (2)" + "\n" + "Engineering: Espanol mecánico (3)" + "\n" + "Random: Vocabulario aleatorio (4)" + "\n")
        #         chosen_program
        #     elif mode == 4:
        #         print(menu2)
        #         chosen_program
        #     elif mode == 5:
        #         help
        #     else:
        #         print("Sorry, this programm currently has only 4 modes available!")
        # except:
        #     print("Invalid input! Please choose a correct Number for the Programm\n")
            

### vocab-set storage: All the vocab sets are stored here ###
def vocabset_storage(language, set):
    kueche = ["Ofen", "Herd", "Kühlschrank", "Kochtopf", "Toaster", "Messer", "Pfanne", "Glas",\
              "Löffel", "Gabel", "Teller", "Spülmaschine", "Spüle", "Pfannenwender", "Gewürze"]
    natur = ["Baum", "Wiese", "Blume", "Park", "Vogel", "Brunnen", "Teich", "Eichhörnchen",\
             "Igel", "Pilz", "Regenbogen", "Wolke", "Schnee", "Regen", "Wetter"]
    mechanisch = ["Winkel", "Kurzschluss", "Achse", "Eichung", "Leitfähigkeit", "Gegengewicht", "Induktivität",\
                  "Dichte", "Gleichung", "Reibung", "Erdung", "messen", "Widerstand", "Spannung", "Kapazität"]
###translations for german category "kueche"
    kitchen = ["oven", "stove", "refrigerator", "pot", "toaster", "knife", "pan", "glass", "spoon",\
               "fork", "plate", "dishwasher", "sink", "spatula", "spices"]                                                  # (List) english translation for "kueche"
    cuisine = ["four", "poêle", "réfrigérateur", "casserole", "grille-pain", "couteau", "poêle", "verre",\
               "cuillère", "fourchette", "assiette", "lave-vaisselle", "évier", "poêle à frire", "épices"]                  # (List) french translation for "kueche"
    cocina = ["horno", "cocina", "refrigerador", "cazuela", "tostadora", "cuchillo", "sartén", "vidrio",\
              "cuchara", "tenedor", "plato", "lavavajillas", "fregadero", "especia"]                                        # (List) spanish translation for "kueche"
### translations for german category "natur"
    nature_en = ["tree", "meadow", "flower", "park", "bird", "well", "pond", "squirrel", "hedgehog",\
                 "mushroom", "rainbow", "cloud", "snow", "rain", "weather"]                                                 # (List) english translation for "natur"
    nature_fr = ["arbre", "prairie", "fleur", "parc", "oiseau", "puits", "étang", "écureuil", "hérisson",\
                 "champignon", "arc en ciel", "nuage", "neige", "pluie", "temps"]                                           # (List) french translation for "natur"
    naturaleza = ["árbol", "prado", "flor", "parque", "pájaro", "pozo", "estanque", "ardilla", "erizo",\
                  "hongo", "arcoíris", "nube", "nieve", "lluvia", "tiempo"]                                                 # (List) spanish translation for "natur"
### translations for german category "mechanisch"
    engineering = ["angle", "short circuit", "axis", "calibration", "conductivity", "counterweight", "inductance",\
                   "density", "equation", "friction", "earthing", "measure", "resistor", "voltage", "capicity"]             # (List) english translation for "mechanisch"
    mecanique = ["angle", "court-circuit", "axe", "étalonnage", "conductibilité", "contrepoids", "inductance",\
                 "densité", "équation", "frottement", "mise à la terre", "mesurer", "résistance", "tension", "capacité"]    # (List) french translation for "mechanisch"
    mecanico = ["ángulo", "cortocircuito", "eje", "contraste", "conductividad", "contrapeso", "inductividad",\
                "densidad", "ecuación", "frotamiento", "toma de tierra", "medir", "resistencia", "voltaje", "capacidad"]    # (List) spanish translation for "mechanisch"
    
    if set == 1:
        if language == 1:
            query(kitchen, kueche, 14)
        elif language == 2:
            query(cuisine, kueche, 15)
        else:
            query(cocina, kueche, 15)
    elif set == 2: 
        if language == 1:
            query(kitchen, natur, 15)
        elif language == 2:
            query(cuisine, natur, 15)
        else:
            query(cocina, natur, 15)

### empty_lists: initializes two empty lists to save the own vocab list of the user ###
def empty_lists():
    term = []
    definition = []
    vocabset_create(term, definition)


### vocabset_create: an own vocab list can be created here ###
def vocabset_create(term, definition):
    x = 0
    number = 0
    newword = input("Fachbegriff: ")        # New technical term is asked
    term.append(newword)                    # New technical term is saved in  list
    newdef = input("Definition: ")          # New definition is asked
    definition.append(newdef)               # New definition is saved in list
    while x == 0:
        continuing = input("Möchtest du ein weiteres Wort hinzufügen? (Y/N) ")
        if continuing == "Y":
            x = 1
            number = number + 1
            vocabset_create(term, definition)
        elif continuing == "N":
            x = 1
            query(term, definition, number)
        else:
            print("Diese Eingabe kann leider nicht verarbeitet werden.")
    

    

### query:  ###
def query(term, definition, language, mode, number):
    try:
        print("Which modus would you like to have?\nGerman to ", language[mode-1], "(1)\n or ", language[mode-1], "to german(2) or a mixed modus (3)?\n-----------------------\nPress (4) to get back to possible programms " )
        modus= input("Press the number of the option you like to have: ")
        
        if modus=="1":
            print("Please translate this word to ", language[modus-1])

        elif modus=="2":
            print("Please translate this word to German:")

        elif modus=="3":
            print("Please translate this word to German or to ", language[modus-1])
        elif modus=="4":
            vocabset_menu(mode)      
    except:
        print("Wrong input, please try again")

# "main-Funktion": Ablaufplan des Programms mit den Funktionen in der richtigen Reihenfolge
selection_menu()