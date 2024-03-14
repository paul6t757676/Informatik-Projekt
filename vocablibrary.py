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
    