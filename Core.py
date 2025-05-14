from datetime import datetime 
import calendar

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
            priorites = "priorites_" + category_select
            if priorites in informations and informations[priorites] == "oui" :
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
       
        print(self.categories_selectionner)
        print(self.priorites)
        
        
        if "epargnes" not in  self.priorites :
            for category in self.categories_selectionner :
                print(category)
                if category in self.priorites :
                    n = len(self.priorites)
                    
                    biblio_budgetaires[category] = (0.5 * self.revenue)//n

                elif category is not "epargnes":

                    biblio_budgetaires[category] = (0.3 * self.revenue) 

                else :

                    biblio_budgetaires[category] = self.revenue * 0.2 
            
            return biblio_budgetaires

        if "epargnes" in self.priorites : 
            for category in self.categories_selectionner :    
                print(category)

                if category is "epargnes" :

                    biblio_budgetaires["epargnes"] = self.revenue * 0.2

                elif category in self.priorites :

                    biblio_budgetaires[category] = (0.45 * self.revenue)
                else :
                    m = len(self.categories_selectionner)
                    r = len(self.priorites)
                    print(m - r)
                    n = m - r
                    if n == 0  or n == 1:
                        biblio_budgetaires[category] = (0.35 * self.revenue)
                    else :
                        biblio_budgetaires[category] = (0.35 * self.revenue)//n

            return biblio_budgetaires

    def regle75_15_10(self) :
         
        biblio_budgetaires = {}
        if "epargnes" not in self.priorites :
            for category in self.categories_selectionner :

                if category in self.priorites :
                    
                    n = len(self.priorites)

                    biblio_budgetaires[category] = (0.75 * self.revenue)//n

                elif category not in self.priorites :

                    biblio_budgetaires[category] = 0.15 * self.revenue

                else :
                    biblio_budgetaires[category] = 0.10 * self.revenue    

            return biblio_budgetaires
        if "epargnes" in self.priorites :
            for category in self.categories_selectionner :
                if category == "epargnes" :

                    biblio_budgetaires["epargnes"] = self.revenue * 0.1
                
                elif category in self.priorites :

                    biblio_budgetaires[category] = (0.6 * self.revenue)

                else :
                    m = len(self.categories_selectionner) 
                    r = len(self.priorites)
                    n = m - r
                    if n == 0 or n == 1 :
                        biblio_budgetaires[category] =( 0.4 * self.revenue) 
                    else :
                        biblio_budgetaires[category] =( 0.4 * self.revenue) // n
            return biblio_budgetaires


     
    def personnaliser(self) :
         
        biblio_budgetaires  = {}
        C = len(self.categories_selectionner)
        if C == 5 : 

            for category in self.categories_selectionner :

                if category == self.__categories[0] :

                    biblio_budgetaires[category] = 0.3 * self.revenue

                if category == self.__categories[1] :
                    
                    biblio_budgetaires[category] = 0.15 * self.revenue

                if category == self.__categories[2] :
                    
                    biblio_budgetaires[category] = 0.18 * self.revenue

                if category == self.__categories[3] :
                    
                    biblio_budgetaires[category] = 0.07 * self.revenue

                if category == self.__categories[4] :
                    
                    biblio_budgetaires[category] = 0.1 * self.revenue

                if category in self.priorites :

                    biblio_budgetaires[category] += 0.1 * self.revenue

            return biblio_budgetaires
        else : 
            for category in self.categories_selectionner :

                if "logement" not in self.__categories :

                    if category == self.__categories[1] :
                    
                        biblio_budgetaires[category] = 0.22 * self.revenue

                    if category == self.__categories[2] :
                        
                        biblio_budgetaires[category] = 0.25 * self.revenue

                    if category == self.__categories[3] :
                        
                        biblio_budgetaires[category] = 0.14 * self.revenue

                    if category == self.__categories[4] :
                        
                        biblio_budgetaires[category] = 0.17 * self.revenue

                    if category in self.priorites :

                        biblio_budgetaires[category] += 0.11 * self.revenue

                    return biblio_budgetaires

                if "alimentation" not in self.__categories : 

                    if category == self.__categories[0] :

                        biblio_budgetaires[category] = 0.33 * self.revenue

                    if category == self.__categories[2] :
                        
                        biblio_budgetaires[category] = 0.21 * self.revenue

                    if category == self.__categories[3] :
                        
                        biblio_budgetaires[category] = 0.10 * self.revenue

                    if category == self.__categories[4] :
                        
                        biblio_budgetaires[category] = 0.3 * self.revenue

                    if category in self.priorites :

                        biblio_budgetaires[category] += 0.115 * self.revenue

                    return biblio_budgetaires

                if "transport" not in self.__categories : 
                    if category == self.__categories[0] :

                        biblio_budgetaires[category] = 0.34 * self.revenue

                    if category == self.__categories[1] :
                        
                        biblio_budgetaires[category] = 0.19 * self.revenue

                    if category == self.__categories[3] :
                        
                        biblio_budgetaires[category] = 0.11 * self.revenue

                    if category == self.__categories[4] :
                        
                        biblio_budgetaires[category] = 0.14 * self.revenue

                    if category in self.priorites :

                        biblio_budgetaires[category] += 0.11 * self.revenue

                    return biblio_budgetaires

                if "sante" not in self.__categories : 

                    if category == self.__categories[0] :

                        biblio_budgetaires[category] = 0.3 * self.revenue

                    if category == self.__categories[1] :
                        
                        biblio_budgetaires[category] = 0.15 * self.revenue

                    if category == self.__categories[2] :
                        
                        biblio_budgetaires[category] = 0.19 * self.revenue

                    if category == self.__categories[4] :
                        
                        biblio_budgetaires[category] = 0.11 * self.revenue

                    if category in self.priorites :

                        biblio_budgetaires[category] += 0.115 * self.revenue

                    return biblio_budgetaires

                if "epargnes" not in self.__categories :
                    
                    if category == self.__categories[0] :

                        biblio_budgetaires[category] = 0.32 * self.revenue

                    if category == self.__categories[1] :
                        
                        biblio_budgetaires[category] = 0.17 * self.revenue

                    if category == self.__categories[2] :
                        
                        biblio_budgetaires[category] = 0.21 * self.revenue

                    if category == self.__categories[3] :
                        
                        biblio_budgetaires[category] = 0.09 * self.revenue

                    if category in self.priorites :

                        biblio_budgetaires[category] += 0.11 * self.revenue

                    return biblio_budgetaires
                   


                

       
    
    def ajouter_depenses_jounalieres_and_recuperer_depenses_mensuelles( self,montant,annee, mois,date = datetime.date) :
        dict_journalier = {}
        liste_depenses = []
        if date is None :
            date = datetime.now()
        
        montant = float(montant)
        for category in self.categories_selectionner : 
        
            dict_journalier[category] = montant  
    
       
        liste_depenses.append(dict_journalier) 
        print(f"\
            {mois}\n\
            {annee}")
        return f"{liste_depenses},{dict_journalier}"
           
    def nombre_jour_en_1mois() :
        aujourdhui = datetime.now()
        mois = aujourdhui.month
        annee = aujourdhui.year
        nombre_jours = calendar.monthrange( year=annee ,month=mois)[1]
        return nombre_jours

        
        
   


            
                
                
                
    

   
    
      