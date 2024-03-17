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
def selection_menu():
    while True:
        print("Wilkommen zu unserem Vokabel-Trainer. Unten finden Sie eine Liste mit verschiedenen Sprachen und weiteren Optionen, zwischen denen Sie wählen können.")
        print("Geben Sie einfach die Nummer des Modus ein, den Sie auswählen wollen und folgen Sie hiernach den Anweisungen des Programmes.")
        print("\nMenu:")
        print("(1) Englisch" + "\n" + "(2) Französisch" + "\n" + "(3) Spanisch" + "\n" + "(4) Erstelle deine eigene Vokabelliste" + "\n" + "(5) Hilfe" + "\n")    
                           #print options
        try:
            mode = int(input("Um eine Sprache auszuwählen, oder um Ihre eigene Liste zu erstellen, geben Sie eine Nummer (1 - 4) ein. Geben Sie '5' ein, um Hilfe zu bekommen: "))  
            os.system('cls' if os.name == 'nt' else 'clear')                                         #select chosen option 
            help = "\nSie brauchen Hilfe? Bei diesem Programm handelt es sich um einen Vokabeltrainer. Er kann Sie dabei unterstützen, Ihre Sprachkenntnisse zu trainieren und zu erweitern, indem es Sie verschiedene Vokabeln abfragt.\
Sie können in den verschiedenen Menüs, verschiedene Modi auswählen. Bei diesen Modi handelt es sich zum einen um unterschiedliche Sprachen und zum andern um einen zusätzlichen Modus, bei welchem Sie ihre eigenen Vokabel-Listen zum lernen erstellen können.\
Die verfügbaren Sprachen sind in der aktuellsten Version Englisch, Französisch und Spanisch. Nach der Sprachauswahl, können Sie noch einmal zwischen unterschiedlichen Vokabel-Paketen wählen Der Rest des Programmes erklärt sich dann von alleine!.\
Sollten Sie ein Mal eine Vokabel falsch übersetzt haben, macht sie das Programm hierauf ebenfalls aufmerksam.\nViel Spaß beim lernen!\n-----------------------"
            if mode == 5:
                print(help)
                selection_menu()
            elif mode<4:
                vocabset_storage(mode)
            elif mode == 4:
                empty_lists()
            else:
                print("Momentan gibt es nur 4 Modi, zwischen denen gewählt werden kann. Bitte geben Sie eine andere Option ein!")
                selection_menu()
        except:
                print("Ungültige Eingabe! Bitte geben Sie einen gültigen Wert ein (1 - 5).\n")
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
    while True:
        try:
            if language == 1:
                print("(1) Kitchen: In the Kitchen" + "\n" + "(2) Nature: Out in the nature" + "\n" + "(3) Engineering: Mechanical English" + "\n" + "(4) Return to Language Menu" + "\n")
                #vocabset_storage(mode, chosen_program)
            elif language==2:
                print("(1) Kitchen: Dans la cuisine" + "\n" + "(2) Nature: Dans la nature" + "\n" + "(3) Engineering: Francais mécanique" + "\n" + "(4) Return to Language Menu" + "\n")
            elif language==3:
                print("Kitchen: En la cocina (1)" + "\n" + "Nature: En la naturaleza (2)" + "\n" + "Engineering: Espanol mecánico (3)" + "\n" + "Return to Language Menu (4)" + "\n")
            elif language==4:
                selection_menu()
            set = int(input("-----------------------\nWählen Sie aus obiger Liste ein spezifisches Thema aus, welches Sie lernen wollen, oder kehren Sie zum Sprach-Menü zurück (1 - 4): "))
            if set == 1:
                if language == 1:
                    query(kitchen, kueche, 14)
                elif language == 2:
                    query(cuisine, kueche, 14)
                else:
                    query(cocina, kueche, 14)
            elif set == 2: 
                if language == 1:
                    query(nature_en, natur, 14)
                elif language == 2:
                    query(nature_fr, natur, 14)
                else:
                    query(naturaleza, natur, 14)
            elif set == 3: 
                if language == 1:
                    query(engineering, mechanisch, 14)
                elif language == 2:
                    query(mecanique, mechanisch, 14)
                else:
                    query(mecanico, mechanisch, 14)
            elif set == 4:
                selection_menu()
        except:
            print("Diese Eingabe kann leider nicht verarbeitet werden! ")


#######################################################################################
### empty_lists: initializes two empty lists to save the own vocab list of the user ###
#######################################################################################
def empty_lists():
    term = []
    definition = []
    vocabset_create(term, definition)


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



##############################################################
### vocabset_create: an own vocab list can be created here ###
##############################################################
def vocabset_create(term, definition):
    x = 0                                                   # saves if the while loop shall be breaked
    newword = input("Fremdwort: ")                          # New technical term is asked
    term.append(newword)                                    # New technical term is saved in  list
    newdef = input("Deutsche Uebersetzung: ")               # New translation is asked
    definition.append(newdef)                               # New translation is saved in list
    while x == 0:
        continuing = input("Moechtest du ein weiteres Wort hinzufuegen? (Y/N) ")    # asks if another word shall be added
        if continuing == "Y":                               # if the answer is yes, the programm continues by calling the funktion again
            x = 1                                           # and breaks the while loop by changing x
            vocabset_create(term, definition)
        elif continuing == "N":                             # if the answer is no, the while loop is broken by changing x 
            x = 1                                           # and the query is started by calling the function "query"
            query(term, definition, len(term)-1)
        else:
            print("Diese Eingabe kann leider nicht verarbeitet werden.")



    
#######################################################################
### query: queries the chosen vocabs with different modes available ###
#######################################################################
def query(term, definition, number):
    print("\n-----------------------\nWelchen Modus moechten Sie waehlen?\n(1) Deutsch zu Fremdsprache \n(2) Fremdsprache zu Deutsch \n \
              (3) Einen Zufalls-Modus\n-----------------------\nDruecken Sie (4) um zu der Sprachauswahl zurueckzukehren " )
    modus = input("Geben Sie die Zahl des Modus ein, welchen sie auswaehlen moechten: ")          # the mode of the query can be chosen

    try:
                       
        if modus=="1":
            print("Es wird Deutsch zu Fremdsprach abgefragt! ")
            outputt = definition                                        # the german words shall be printed by the program
            inputt = term                                               # the foreign words shall be written by the user

        elif modus=="2":
            print("Es wird Fremdsprache zu Deutsch abgefragt! ")
            outputt = term                                              # the foreign words shall be printed by the program
            inputt = definition                                         # the german words shall be written by the user

        elif modus=="3":
            print("Es wird zufaellig abgefragt! ")                      # continues in random_query

        elif modus=="4":
            selection_menu()                                             # returns to choosing the language
    except:
        print("Falsche Eingabe, bitte versuchen Sie es erneut")
    continuing = True                                                           # True if the query shall be continued, False if it shall be ended
    counter = 0
    statussafe = query_status_safe(number)
    
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
            print("Bitte geben Sie die Übersetzung von ", word, " ein: ")
            translation = input()
            if translation == inputt[vocabnumber]:                                     # checks if the answer is right
                statussafe[vocabnumber] = True                                       # notices the vocab as right translated
                print("Richtig!")
                counter += 1  
            else:
                print("Die Antwort war leider falsch! Die korrekte Antwort wäre gewesen: ",inputt[vocabnumber])
            if counter == number + 1:                                           # stops while-loop if all vocabs were translated correctly
                continuing = False
                print("Sie haben alle Vokabeln richtig uebersetzt!\nGlueckwunsch!")
                while True:
                    try:
                        menu = input("Was möchten Sie als naechstes tun?\n(1) Das Vokabelset wiederholen\n(2) Zurueck zum Hauptmenue\n(3) Programm beenden\n")
                        match menu:
                            case "1":
                                query(term, definition, number)
                            case "2":
                                selection_menu()
                            case "3":
                                print("Programm wird beendet")
                                print(quit())
                    except:
                        print("Diese Eingabe kann nicht verarbeitet werden!")

            else: 
                c = input("Druecken Sie Enter, um fortzufahren, oder N, um ins Hauptmenue zurueckzukehren!")
                if c == "N":
                    continuing = False
                    selection_menu()                                           # jumps back into the selection menu if N was chosen


##########################################################
### main-function: defines the process of the programm ###
##########################################################
def main():
    selection_menu()                


##############
### Start: ###
##############
main()
