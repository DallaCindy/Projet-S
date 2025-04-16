# from datetime import datetime , timedelta
# from dateutil.relativedelta import relativedelta

# def afficher_date_un_mois_apres(date_entree):
#     date_obj = datetime.strptime(date_entree, '%Y-%m-%d')
#     date_un_mois_apres = date_obj + relativedelta(months=1)
#     return date_un_mois_apres.strftime('%Y-%m-%d')

#     # Convertir la chaîne de caractères en objet datetime
#     # Ajouter un mois à la date
#     # Retourner la date au format 'YYYY-MM-DD'
# # Exemple d'utilisation
# date_input = input("Entrez une date au format YYYY-MM-DD : ")
# print("La date un mois après est :", afficher_date_un_mois_apres(date_input))

liste_principale = [1, 2, 3, 4, 5, [2, 3]]

# Extraire la sous-liste (ici, on suppose que c'est le dernier élément)
sous_liste = liste_principale[-1]

# Sélectionner les éléments qui sont dans liste_principale mais pas dans sous_liste
resultat = [elem for elem in liste_principale if elem not in sous_liste and not isinstance(elem, list)]

print(resultat)  # Affiche : [1, 4, 5]