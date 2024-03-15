##################################################
##                                              ##
##              Vokabeltrainer                  ##
##                                              ##
##################################################

# authors: Paula Stegmayer, Finn Wohnig, Paul Schabram
# date:  07.03.2024
# brief:   This program is a vocab-trainer. It is designed and programmed to train different languages and different topic-specific vocabulary

################################################################################################################
### selection-menu: The preferred language, creating an own vocab list or a help function can be chosen here ###
################################################################################################################

import os           ### imported os library, the os library is used to have an easy way to clear the console when heading to another menu (found on stackoverflow.com)
import vocablibrary
import random       ### imported random library to generate random numbers for the query
import sys          ### imported sys library to stop the programm
def selection_menu():
    while True:
        print("Welcome to our vocab-trainer. Below you find a list of different languages and other options to select." + "\n" + "Just enter the number of the mode you'd like to train and follow the instructions.")
        print("\nMenu:")
        print("(1) English" + "\n" + "(2) French" + "\n" + "(3) Spanish" + "\n" + "(4) Create your own vocab-list" + "\n" + "(5) Help" + "\n")    
                           #print options
        try:
            mode = int(input("To select a Language or to create your own vocab-list, enter a number(1 - 4). Enter '5' to get help: "))  
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
                selection_menu()

#####################################################################
### vocabset_menu: one of the available vocab lists can be chosen ###
#####################################################################
def vocabset_menu(mode):
    language = ["English", "French", "Spanish", "Create your own list:", help] 
    menu2 = print("Language chosen: " , (language[mode-1]),"\n-----------------------\nPossible Topics:\n")
    english = ["Kitchen: In the Kitchen (1)", "Nature: Out in the nature (2)", "Engineering: Mechanical English (3)", "Return to Language Menu (4)"]
    french = ["Kitchen: Dans la cuisine (1)", "Nature: Dans la nature (2)", "Engineering: Francais mécanique (3)", "Return to Language Menu (4)"]
    spanish = ["Kitchen: En la cocina (1)", "Nature: En la naturaleza (2)", "Engineering: Espanol mecánico (3)", "Return to Language Menu (4)"]
    modetranslation = [english, french, spanish]

    while True:
        try:
            if mode == 1:
                print("Kitchen: In the Kitchen (1)" + "\n" + "Nature: Out in the nature (2)" + "\n" + "Engineering: Mechanical English (3)" + "\n" + "Random: Random Vocabs (4)" + "\n")
                #vocabset_storage(mode, chosen_program)
            elif mode==2:
                print("Kitchen: Dans la cuisine (1)" + "\n" + "Nature: Dans la nature (2)" + "\n" + "Engineering: Francais mécanique (3)" + "\n" + "Random: Vocabulaire aléatoire (4)" + "\n")
            elif mode==3:
                print("Kitchen: En la cocina (1)" + "\n" + "Nature: En la naturaleza (2)" + "\n" + "Engineering: Espanol mecánico (3)" + "\n" + "Random: Vocabulario aleatorio (4)" + "\n")
            elif mode==4:
                selection_menu()
            #menu2 =  (print(modetranslation[mode-1]))
            chosen_program = int(input("-----------------------\nChoose one specific vocab-unit you'd like to train (1 - 4): "))
            vocabset_storage(mode, chosen_program)
        except:
            print("Diese Eingabe kann leider nicht verarbeitet werden! ")

    
       
            
#############################################################
### vocab-set storage: All the vocab sets are stored here ###
#############################################################
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
            query(cuisine, kueche, 14)
        else:
            query(cocina, kueche, 14)
    elif set == 2: 
        if language == 1:
            query(kitchen, natur, 14)
        elif language == 2:
            query(cuisine, natur, 14)
        else:
            query(cocina, natur, 14)
    elif set == 3: 
        if language == 1:
            query(engineering, mechanisch, 14)
        elif language == 2:
            query(mecanique, mechanisch, 14)
        else:
            query(mecanico, mechanisch, 14)

#######################################################################################
### empty_lists: initializes two empty lists to save the own vocab list of the user ###
#######################################################################################
def empty_lists():
    term = []
    definition = []
    vocabset_create(term, definition)

##############################################################
### vocabset_create: an own vocab list can be created here ###
##############################################################
def vocabset_create(term, definition):
    x = 0
    number = 0
    newword = input("Fachbegriff: ")        # New technical term is asked
    term.append(newword)                    # New technical term is saved in  list
    newdef = input("Übersetzung: ")         # New translation is asked
    definition.append(newdef)               # New translation is saved in list
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


#################################################################################################
### query_status_safe: creates a list to safe if a word was translated correctly in the query ###   
#################################################################################################
def query_status_safe(number):
    x = 0
    statussafe = []
    while x <= number:
        statussafe.append(False)
        x += 1
    return statussafe


    
#######################################################################
### query: queries the chosen vocabs with different modes available ###
#######################################################################
def query(term, definition, number):
    print("\n-----------------------\nWelchen Modus möchten Sie wählen?\n(1) Deutsch zu Fremdsprache \n(2) Fremdsprache zu Deutsch \n \
              (3) Einen Zufalls-Modus\n-----------------------\nDrücke Sie (4) um zu der Themenwahl zurückzukehren " )
    modus = input("Geben Sie die Zahl des Modus ein, welchen sie auswählen möchten: ")          # the mode of the query can be chosen

    try:
                       
        if modus=="1":
            print("Es wird Deutsch zu Fremdsprach abgefragt! ")
            statussafe = query_status_safe(number)                      # creates a list to safe the known german words
            output = definition
            inputt = term

        elif modus=="2":
            print("Es wird Fremdsprache zu Deutsch abgefragt! ")
            statussafe = query_status_safe(number)                      # creates a list to safe the known foreign words
            output = term
            inputt = definition

        elif modus=="3":
            print("Es wird zufällig abgefragt! ")
            random_query(term, definition, number)                      # continues in random_query
        elif modus=="4":
            vocabset_menu()                                             # returns to choosing the vocabset
    except:
        print("Falsche Eingabe, bitte versuchen Sie es erneut")
    continuing = True                                                           # True if the query shall be continued, False if it shall be ended
    counter = 0
    while continuing == True:
        vocab = random.uniform(0, number)
        if statussafe[vocab] == False:                                          # checks if the vocab has already been translated correctly
            translation = input("Bitte geben Sie die Übersetzung von ", output[vocab], " ein: " )
            if translation == inputt[vocab]:                                     # checks if the answer is right
                statussafe[vocab] == True                                       # notices the vocab as right translated
                print("Richtig!")
                counter =+ 1                                                    # counts the word as right translated
            else:
                print("Die Antwort war leider falsch!")
            if counter == number + 1:                                           # stops while-loop if all vocabs were translated correctly
                continuing = False
                print("Sie haben alle Vokabeln richtig übersetzt!\nGlückwunsch!")
                while True:
                    try:
                        menu = int(input("Was möchten Sie als nächstes tun?\n(1) Das Vokabelset wiederholen\n(2) Zurück zum Hauptmenü\n(3) Programm beenden"))
                        match menu:
                            case 1:
                                query(term, definition, number)
                            case 2:
                                selection_menu()
                            case 3:
                                print("Programm wird beendet")
                                sys.exit()
                    except:
                        print("Diese Eingabe kann nicht verarbeitet werden!")

            else: 
                c = input("Drücken Sie Enter, um fortzufahren, oder N, um ins Hauptmenue zurueckzukehren!")
                if c == "N":
                    continuing = False
                    selection_menu()                                           # jumps back into the selection menu if N was chosen
            
                


def random_query(term, definition, number):
    statussafe_de = query_status_safe(number)                   # creates a list to safe the known german word
    statussafe_fo = query_status_safe(number)                   # creates a list to safe the known foreign words

# "main-Funktion": Ablaufplan des Programms mit den Funktionen in der richtigen Reihenfolge
selection_menu()