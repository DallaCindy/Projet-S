# # from datetime import datetime , timedelta
# # from dateutil.relativedelta import relativedelta

# # def afficher_date_un_mois_apres(date_entree):
# #     date_obj = datetime.strptime(date_entree, '%Y-%m-%d')
# #     date_un_mois_apres = date_obj + relativedelta(months=1)
# #     return date_un_mois_apres.strftime('%Y-%m-%d')

# #     # Convertir la chaîne de caractères en objet datetime
# #     # Ajouter un mois à la date
# #     # Retourner la date au format 'YYYY-MM-DD'
# # # Exemple d'utilisation
# # date_input = input("Entrez une date au format YYYY-MM-DD : ")
# # print("La date un mois après est :", afficher_date_un_mois_apres(date_input))

# liste_principale = [1, 2, 3, 4, 5, [2, 3]]

# # Extraire la sous-liste (ici, on suppose que c'est le dernier élément)
# sous_liste = liste_principale[-1]

# # Sélectionner les éléments qui sont dans liste_principale mais pas dans sous_liste
# resultat = [elem for elem in liste_principale if elem not in sous_liste and not isinstance(elem, list)]



def definir_revenu_mensuel(revenu: float) -> None:
    """
    Enregistre ou met à jour le revenu mensuel de l'utilisateur.
    Args:
        revenu: Montant du revenu mensuel
    """
    pass

def definir_categories_budgetaires(categories: Dict[str, bool]) -> None:
    """
    Définit les catégories budgétaires actives.
    Args:
        categories: Dictionnaire nom_categorie -> True/False
    """
    pass


def definir_priorites(priorites: List[str]) -> None:
    """
    Définit l'ordre de priorité parmi les catégories sélectionnées.
    Args:
        priorites: Liste ordonnée de noms de catégories actives
    """
    pass


def ajouter_depense_journaliere(
    montant: float,
    categorie: str,
    date: Optional[datetime.date] = None,
    note: str = ""
) -> None:
    """
    Enregistre une dépense journalière.
    Args:
        montant: Montant dépensé
        categorie: Catégorie (doit être active)
        date: Date de la dépense (par défaut aujourd'hui)
        note: Commentaire facultatif
    """
    if date is None:
        date = datetime.date.today()
    pass


def recuperer_depenses_mensuelles(annee: int, mois: int) -> List[Dict]:
    """
    Récupère la liste des dépenses pour un mois donné.
    Returns:
        Liste de dicts avec clés: montant, categorie, date, note
    """
    pass


def calculer_somme_par_categorie(annee: int, mois: int) -> Dict[str, float]:
    """
    Calcule le total des dépenses par catégorie pour le mois.
    Returns:
        Dictionnaire nom_categorie -> montant_total
    """
    pass


def calculer_resume_global(annee: int, mois: int, revenu:
Optional[float] = None) -> Dict[str, float]:
    """
    Calcule revenu, dépenses totales et solde estimé pour le mois.
    Args:
        revenu: Montant du revenu mensuel (optionnel si déjà défini)
    Returns:
        { 'revenu': float, 'depenses': float, 'solde': float }
    """
    pass


def generer_rapport_mensuel(annee: int, mois: int) -> str:
    """
    Génère un rapport mensuel (PDF/CSV) et renvoie le chemin du fichier.
    """
    pass


def envoyer_notification(message: str, quand: datetime.datetime) -> None:
    """
    Planifie l'envoi d'une notification locale à l'utilisateur.
    Args:
        message: Contenu de la notification
        quand: Date et heure d'envoi
    """
    pass


def alerter_seuil_budget(categorie: str, seuil: float) -> bool:
    """
    Vérifie si les dépenses d'une catégorie ont atteint un seuil et
retourne True si alerte.
    Args:
        categorie: Nom de la catégorie à surveiller
        seuil: Seuil de dépenses
    """
    pass


 # try :
                #     category is not "epargnes"
                # except "ConseilEpargne" :
                #     print("\
                #             Je comprends que ce n'est pas toujours évident, mais prendre l'habitude d'épargner, \n\
                #             même un petit peu, c'est une excellente démarche pour assurer ton avenir.\
                #             ")
                # else :
                #     category = self.revenue * 0,2
                # #     biblio_budgetaires[category] = self.revenue * 0,2 
                # return f"\
                #     affichage plus conseil et expliction"