# Grille de lettres
grille = [
    ['B', 'O', 'N', 'N', 'E'],
    ['I', 'G', 'O', 'I', 'J'],
    ['E', 'L', 'I', 'O', 'I'],
    ['N', 'Q', 'R', 'S', 'T'],
    ['S', 'V', 'W', 'X', 'Y']
]

# Mots cachés
mots_caches = ['BONNE', 'BIENS', 'LOI', 'NOIR']

# Fonction pour trouver les mots cachés
def trouver_mots_caches(grille, mots_caches):
    mots_trouves = set()
    taille_grille = len(grille)

    for mot_cache in mots_caches:
        trouve = False
        for ligne in grille:
            mot = ''.join(ligne)
            if mot_cache in mot:
                mots_trouves.add(mot_cache)
                trouve = True
                break
        
        if not trouve:
            for colonne in range(taille_grille):
                mot = ''.join([grille[ligne][colonne] for ligne in range(taille_grille)])
                if mot_cache in mot:
                    mots_trouves.add(mot_cache)
                    trouve = True
                    break
        
        if not trouve:
            mots_trouves.add("Non trouvé")

    return mots_trouves

# Affichage de la grille de lettres
print("Grille de lettres :")
for ligne in grille:
    print(' '.join(ligne))
print()

# Nombre de mots au départ
nombre_mots_depart = len(mots_caches)
print(f"Nombre de mots à trouver : {nombre_mots_depart}\n")

# Demander à l'utilisateur de saisir les réponses
reponses = set()
continuer = True

while continuer and len(reponses) < nombre_mots_depart:
    reponse = input("Entrez un mot caché : ").upper()
    
    if reponse in mots_caches and reponse not in reponses:
        print(f"Le mot '{reponse}' a été trouvé !\n")
        reponses.add(reponse)
        mots_restants = nombre_mots_depart - len(reponses)
        print(f"Il reste {mots_restants} mot(s) à trouver.\n")
    else:
        print(f"Le mot '{reponse}' n'a pas été trouvé ou a déjà été trouvé.\n")
    
    if mots_restants == 0:
        break
    
    continuer = input("Voulez-vous continuer ? (Oui/Non): ").lower() == "oui"

# Appel de la fonction pour trouver les mots cachés
resultats = trouver_mots_caches(grille, reponses)

# Affichage des résultats
print("\nRésultats :")
for mot_trouve in resultats:
    print(f"Le mot '{mot_trouve}'")

# Félicitations si tous les mots ont été trouvés
if len(resultats) == nombre_mots_depart:
    print("Félicitations ! Vous avez trouvé tous les mots.")
