from datetime import datetime


class Core:

    __categories = ["logement", "alimentation", "transport", "sante", "epargnes"]

    revenue = 0
    categories_selectionner = []
    priorites = []

    dict_depenses_journalieres = {}

    def __init__ (self, informations):
        self.definir_revenue_mensuel(informations)
        self.definir_categories_budgetaires(informations)
        self.definir_priorites(informations)
        self.ajouter_depenses_jounalieres(informations)
        

    def definir_revenue_mensuel(self, informations) :
        self.revenue = float(informations["user_revenue"])

    def definir_categories_budgetaires(self, informations) :
        for category in self.__categories:
            if category in informations and informations[category] == "oui":
                self.categories_selectionner.append(category)

    def definir_priorites(self, informations) :
        for category_select in self.categories_selectionner :
            if category_select in informations and informations[category_select] == "oui" :
                self.priorites.append(category_select)

    def ajouter_depenses_jounalieres(self, informations, date = datetime.date) :

        if date is None :
            date = datetime.now()

        for category in self.categories_selectionner :

            old = 'user_old_' + category
            if old in informations:
                self.dict_depenses_journalieres[category] = informations[old]

    def regle50_30_20(self) :

        biblio_budgetaires = {}

        for category in self.categories_selectionner :

            if category in self.priorites :
                n = len(self.priorites)
                
                biblio_budgetaires[category] = (0.5 * self.revenue)/n

            elif category is not "epargnes":

                biblio_budgetaires[category] = (0.3 * self.revenue) 

            else :

                biblio_budgetaires[category] = self.revenue * 0.2 
               
        return biblio_budgetaires
    

    def regle75_15_10(self) :
         
        biblio_budgetaires = {}

        for category in self.categories_selectionner :

            if category in self.priorites :
                
                n = len(self.priorites)

                biblio_budgetaires[category] = (0,75 * self.revenue)/n

            elif category is not self.priorites :

                biblio_budgetaires[category] = 0.15 * self.revenue

            else :
                biblio_budgetaires[category] = 0,1 * self.revenue    

        return biblio_budgetaires
     
    def personnaliser(self) :
         
        biblio_budgetaires  = {}

        for category in self.categories_selectionner :

            if category == self.__categories[0] :

                biblio_budgetaires[category] = 0,3 * self.revenue

            if category == self.__categories[1] :
                
                biblio_budgetaires[category] = 0,15 * self.revenue

            if category == self.__categories[2] :
                
                biblio_budgetaires[category] = 0,18 * self.revenue

            if category == self.__categories[3] :
                
                biblio_budgetaires[category] = 0,07 * self.revenue

            if category == self.__categories[4] :
                
                biblio_budgetaires[category] = 0,1 * self.revenue
        
        return biblio_budgetaires
            



            
        

    