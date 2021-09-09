import random
# Définition des symboles, de la matrice des résultats du match et de l'équivalent numérique des symboles
symboles = ["Pierre","Papier","Ciseaux","Lezard","Spock"]
equiv = [1,2,3,4,5]
combis = [None, False, False, True , True],[True, None, False, False, True], [True, True, None, False, False], [False, True, True, None, False], [False, False, True, True, None]

# Définition du joueur 1
while(True):
    J1 = input("Pierre, Papier, Ciseaux, Lezard, Spock: ")
    while(J1 not in symboles):
          J1 = input("Choix invalide ! Choisissez à nouveau : ")
    print("J1 =",J1)

    # Définition du joueur 2
    Choix_J2 = random.randint(0,4)
    J2 = symboles[Choix_J2]
    while(J2 == J1):
        Choix_J2 = random.randint(0,4)
        J2 = symboles[Choix_J2]
    print("J2 =",J2)

    # Récupération du résultat en fonction des choix
    J1_equiv = symboles.index(J1)
    J2_equiv = symboles.index(J2)
    result = combis[J1_equiv][J2_equiv]

    # Affichage final
    if(result == True): 
        print("Le Joueur 1 a gagner")
    elif(result == False): 
        print("Le Joueur 2 a gagner")
        
    continue_game = input("Voulez-vous rejouer(y/n): ")
    while(continue_game != "y" and continue_game != "n"):
        continue_game = input("Voulez-vous rejouer(y/n)")
    if(continue_game == "n"):
        break;
    if(continue_game == "y"):
        print("Début de la nouvelle partie !")