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
import creating
import random       ### imported random library to generate random numbers for the query
import sys          ### imported sys library to stop the programm
os.system('cls' if os.name == 'nt' else 'clear')
def selection_menu():
    while True:
        print("Wilkommen zu unserem Vokabel-Trainer. Hier finden Sie eine Liste mit verschiedenen Sprachen \
und weiteren Optionen, zwischen welchen Sie wählen können.\n\
Geben Sie die Nummer des Modus ein, den Sie auswählen wollen und folgen Sie den Anweisungen des Programmes.")
        print("\nMenu:")
        print("(1) Englisch" + "\n" + "(2) Französisch" + "\n" + "(3) Spanisch" + "\n" + \
"(4) Erstellen Sie eine eigene Vokabelliste" + "\n" + "(5) Hilfe" + "\n")    
                           #print options
        try:
            mode = int(input("Geben Sie einen Modus ein, welchen Sie auswählen möchten (1-5): "))  
            os.system('cls' if os.name == 'nt' else 'clear')                                          
            help = "\nSie brauchen Hilfe? Bei diesem Programm handelt es sich um einen Vokabeltrainer.\nEr kann Sie \
dabei unterstützen, Ihre Sprachkenntnisse zu trainieren und zu erweitern, indem er Sie verschiedene Vokabeln abfrägt.\n\
Sie können in den verschiedenen Menüs, verschiedene Modi auswählen. Bei diesen Modi handelt es sich zum einen \num \
unterschiedliche Sprachen und zum andern um einen zusätzlichen Modus, bei welchem Sie ihre eigenen Vokabel-Listen zum Lernen erstellen können. \n\
Die verfügbaren Sprachen sind in der aktuellsten Version Englisch, Französisch und Spanisch. \nNach der Sprachauswahl, \
können Sie noch einmal zwischen unterschiedlichen Vokabel-Paketen wählen. \n\
Sollten Sie eine Vokabel falsch übersetzt haben, macht Sie das Programm hierauf aufmerksam.\nViel Spaß beim Lernen!\n-----------------------"
            if mode == 5:                                                                                                       # prints a help text
                print(help)
                selection_menu()
            elif mode<4 and mode > 0:
                vocabset_storage(mode)                                                                                          # calls vocabset_storage
                return
            elif mode == 4:                                                                                                     # calls empty_lists to create an own list
                empty_lists()
                return
            elif mode < 1:
                print("Ungültige Eingabe! Bitte geben Sie einen gültigen Wert ein (1 - 5).\n-----------------------\n")
                selection_menu()
            else:
                print("Momentan gibt es nur 4 Modi, zwischen denen gewählt werden kann. Bitte geben Sie eine andere Option ein!\n-----------------------\n")
                selection_menu()
        except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ungültige Eingabe! Bitte geben Sie einen gültigen Wert ein (1 - 5).\n-----------------------\n")
                selection_menu()



#############################################################
### vocab-set storage: All the vocab sets are stored here ###
#############################################################
def vocabset_storage(language):
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
              "cuchara", "tenedor", "plato", "lavavajillas", "espátula", "fregadero", "especia"]                                        # (List) spanish translation for "kueche"
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
    while True:
        try:
            if language == 1:                                                                             # prints the fitting vocab list options based on the chosen language
                print("(1) Kitchen: In the Kitchen" + "\n" + "(2) Nature: Out in the nature" + \
                      "\n" + "(3) Engineering: Mechanical English" + "\n" + "(4) Zur Sprachauswahl zurückkehren" + "\n")
                #vocabset_storage(mode, chosen_program)
            elif language==2:
                print("(1) Kitchen: Dans la cuisine" + "\n" + "(2) Nature: Dans la nature" + "\n" + \
                      "(3) Engineering: Francais mécanique" + "\n" + "(4) Zur Sprachauswahl zurückkehren" + "\n")
            elif language==3:
                print("(1) Kitchen: En la cocina" + "\n" + "(2) Nature: En la naturaleza" + "\n" + \
                      "(3) Engineering: Espanol mecánico" + "\n" + "(4) Zur Sprachauswahl zurückkehren" + "\n")
            elif language==4:
                selection_menu()                                                                                            # returns to selection menu
            set = int(input("-----------------------\nWählen Sie aus obiger Liste ein spezifisches Thema aus, \
welches Sie lernen wollen, oder kehren Sie zum Sprach-Menü zurück (1 - 4): "))                                              # asks which list was chosen
            os.system('cls' if os.name == 'nt' else 'clear')
            if set == 1:                                                                                                    # calls query with the chosen vocab lists
                if language == 1:
                    query(kitchen, kueche, 14)
                    return
                elif language == 2:
                    query(cuisine, kueche, 14)
                    return
                else:
                    query(cocina, kueche, 14)
                    return
            elif set == 2: 
                if language == 1:
                    query(nature_en, natur, 14)
                    return
                elif language == 2:
                    query(nature_fr, natur, 14)
                    return
                else:
                    query(naturaleza, natur, 14)
                    return
            elif set == 3: 
                if language == 1:
                    query(engineering, mechanisch, 14)
                    return
                elif language == 2:
                    query(mecanique, mechanisch, 14)
                    return
                else:
                    query(mecanico, mechanisch, 14)
                    return
            elif set == 4:
                selection_menu()                                                                                            # returns to selection menu
            elif set >4 or set < 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Dieser Modus existiert leider nicht!\n-----------------------\n ")
        except:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Diese Eingabe kann leider nicht verarbeitet werden!\n-----------------------\n ")

#######################################################################################
### empty_lists: initializes two empty lists to save the own vocab list of the user ###
#######################################################################################
def empty_lists():
    term = []
    definition = []                             # creates two empty lists
    vocabset_create(term, definition)           # goes to vocabset create with the empty lists
    return


#################################################################################################
### query_status_safe: creates a list to safe if a word was translated correctly in the query ###   
#################################################################################################
def query_status_safe(number):
    x = 0
    statussafe = []                     # creates an empty list
    while x <= number:                  # checks if the list is as long as the list of vocabs
        statussafe.append(False)        # if not, it adds another subject to the list
        x += 1                          
    return statussafe                   # returns the finished list



##############################################################
### vocabset_create: an own vocab list can be created here ###
##############################################################
def vocabset_create(term, definition):
    x = 0                                                   # saves if the while loop shall be breaked
    newword = input("Fremdwort: ")                          # New technical term is asked
    term.append(newword)                                    # New technical term is saved in  list
    newdef = input("Deutsche Übersetzung: ")               # New translation is asked
    definition.append(newdef)                               # New translation is saved in list
    while x == 0:
        continuing = input("Möchten Sie ein weiteres Wort hinzufügen? (Y/N) ")    # asks if another word shall be added
        if continuing == "Y":                               # if the answer is yes, the programm continues by calling the funktion again
            x = 1                                           # and breaks the while loop by changing x
            vocabset_create(term, definition)
        elif continuing == "N":                             # if the answer is no, the while loop is broken by changing x 
            x = 1                                           # and the query is started by calling the function "query"
            os.system('cls' if os.name == 'nt' else 'clear')
            query(term, definition, len(term)-1)
            return
        else:
            print("Diese Eingabe kann leider nicht verarbeitet werden.")



    
#######################################################################
### query: queries the chosen vocabs with different modes available ###
#######################################################################
def query(term, definition, number):
    print("Welchen Modus möchten Sie wählen?\n(1) Deutsch zu Fremdsprache \n(2) Fremdsprache zu Deutsch \n\
(3) Einen Zufalls-Modus\n-----------------------\nDrücken Sie (4) um zu der Themenwahl zurückzukehren " )
    modus = input("\nGeben Sie die Zahl des Modus ein, welchen sie auswählen möchten: ")          # the mode of the query can be chosen
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
                       
        if modus=="1":
            print("Es wird Deutsch zu Fremdsprache abgefragt! ")
            outputt = definition                                        # the german words shall be printed by the program
            inputt = term                                               # the foreign words shall be written by the user

        elif modus=="2":
            print("Es wird Fremdsprache zu Deutsch abgefragt! ")
            outputt = term                                              # the foreign words shall be printed by the program
            inputt = definition                                         # the german words shall be written by the user

        elif modus=="3":
            print("Es wird zufällig abgefragt! ")                      # continues by choosing the asked language randomly

        elif modus=="4":
            selection_menu()                                            # returns to choosing the language
    except:
        print("Falsche Eingabe, bitte versuchen Sie es erneut")
    continuing = True                                                   # True if the query shall be continued, False if it shall be ended
    counter = 0                                                         # counts how many words have been translated correctly
    statussafe = query_status_safe(number)                              # creates a list to safe if a word has been translated correctly
    score = 0                                                           # creates score to save the earned points
    while continuing == True:
        if modus == "3":
            random_direction = random.randint(0, 1)                         # creates a random number to decide which direction is asked
            if random_direction == 0:                                       # if the number is 0, the foreign word gets asked
                outputt = term
                inputt = definition
            else:                                                           # if the number is 1, the german word gets asked
                outputt = definition
                inputt = term
        vocabnumber = random.randint(0, number)
        word = outputt[vocabnumber]
        if statussafe[vocabnumber] == False:                                          # checks if the vocab has already been translated correctly
            print("-----------------------\nBitte geben Sie die Übersetzung von ", word, " ein: ")
            translation = input()
            if translation == inputt[vocabnumber]:                                     # checks if the answer is right
                statussafe[vocabnumber] = True                                       # notices the vocab as right translated
                print("Richtig!")
                score += 100                                                # increases the score with 100
                print("\n-----------------------\nSie haben 100 Punkte erhalten!\nIhr neuer Score beträgt: ", score)
                counter += 1                                                # updates the counter of right answers
            else:
                print("\nDie Antwort war leider falsch! Die korrekte Antwort wäre gewesen: ",inputt[vocabnumber])
                score -= 50                                                # decreases the score with 100
                print("\n-----------------------\nSie haben 50 Punkte verloren!\nIhr neuer Score beträgt: ", score)
            if counter == number + 1:                                           # stops while-loop if all vocabs were translated correctly
                continuing = False
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Sie haben alle Vokabeln richtig übersetzt!\nGlückwunsch!\n-----------------------\nIhr Endscore beträgt: ", score)
                while True:
                    try:
                        menu = input("-----------------------\nWas möchten Sie als nächstes tun?\n\n(1) Das Vokabelset wiederholen\n\
(2) Zurueck zum Hauptmenü\n(3) Programm beenden\n")    # asks what the user wants to do now
                        os.system('cls' if os.name == 'nt' else 'clear')
                        match menu:
                            case "1":
                                query(term, definition, number)             # restarts the query with the same words
                            case "2":
                                selection_menu()                            # returns to the selection menu
                            case "3":
                                print("Programm wird beendet")
                                return
                    except:
                        print("Diese Eingabe kann nicht verarbeitet werden!")

            else: 
                c = input("-----------------------\nDrücken Sie (Enter) um fortzufahren, oder (N) um ins Hauptmenü zurückzukehren!")
                os.system('cls' if os.name == 'nt' else 'clear')
                if c == "N":
                    continuing = False
                    selection_menu()                                        # jumps back into the selection menu if N was chosen
               


##############
### Start: ###
##############
selection_menu()
sys.exit()                                                                  # closes the program by using the sys-library
