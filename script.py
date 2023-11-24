# Test
livre = "Moby dick"
print(livre)

# Exercice 1, F-string et variables
nom = "Damien"
age = 27
print(f"Je m'appelle {nom} et j'ai {age} ans.")
age = int(age) + 10
print(f"Je m'appelle {nom} et j'ai {age} ans.")

# Exercice 2, variables bool, float, int
duree_episode = 20
pourcentage = 3.2
succes = True
sentence = "Oui bonjour, c'est josé à l'appareil"
print(type(age))

# Exercice 3, reconnaître les types de variables
nom = "Damien"
age = 27
taille = 1.70
est_etudiant = True
print(nom, age, taille, est_etudiant)
print(type(nom), type(age), type(taille), type(est_etudiant))

# Exercice 4, Listes
voitures = ["Peugeot 207", "Renault Clio", "Porsche Carrera", "Tesla model 3"]
print(voitures[0])
liste_phrase = "Bodjour, je suis une longue phrase et aussi une liste."
print(liste_phrase[2])
voitures.append("Peugeot 308")
voitures.remove("Peugeot 207")
print(voitures)
print(len(voitures))
print(len(liste_phrase))
voitures.sort()
print(voitures)
voitures.extend("Nissan GTR")
voitures.insert(1, "test 2éme position")
print(voitures)
voitures.pop() #Suppression last element
voitures.index("Peugeot 308")
voitures.count("Peugeot 207")
voitures.reverse()
print(voitures)

#Exercice 5 tuples (inchangeable)
voitures_definitives = ("Peugeot 207", "Hyundai Getz")
print("Peugeot 207" in voitures_definitives)


# Exercice 6, retest
fruits = ["pomme", "banane", "orange"]
fruits.append("kiwi")
fruits.remove("orange")
fruits[1] = "ananas"
print(len(fruits))
fruits.sort()
print(fruits)


# Les dictionnaires
utilisateur_0 = {}
utilisateur_0["nom"] = "Damien"
utilisateur_0["age"] = 27

utilisateur_1 = {
    nom: "Daphné",
    age: 28
}
print(utilisateur_1[nom], utilisateur_1[age], "ans.")
print(utilisateur_0)

utilisateur_2 = dict()
print(nom in utilisateur_2)
del utilisateur_1[nom]
print(utilisateur_1)

# Exercice 7. Test dico
fruits = {"pomme": "rouge", "banane": "jaune", "orange": "orange"}
fruits["kiwi"] = "vert"
couleur_banane = fruits["banane"]
fruits["pomme"] = "vert"
del fruits["banane"]
print(fruits)