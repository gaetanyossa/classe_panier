class Article:
      def __init__(self, nom, montant):
        self.nom = nom
        self.montant = montant
        
      def afficher_article(self):
        print(f"Nom: {self.nom}, Montant: {self.montant}")
    
      def ajouter_remise(self, remise_en_prc):
        remise = self.montant*remise_en_prc
        self.montant = self.montant - remise
        
class Panier:
      def __init__(self, nb_articles = 0, mt_articles = 0, articles = []):
          self.nb_articles = nb_articles
          self.mt_articles = mt_articles
          self.articles = articles
    
    # Ajout d'article
      def ajouter_article(self, article):
         if isinstance(article, Article):
            self.nb_articles+=1
            self.articles.append(article)
            self.mt_articles += article.montant
         else:
            print("Ce n'est pas un article")
            
    # Retirer article 
      def retirer_article(self, article):
         if article in self.articles:
            self.nb_articles-=1
            self.articles.remove(article)
            self.mt_articles -= article.montant
         else:
            print("L'article n'est pas dans le panier")
            
    # Vider panier
      def vider_panier(self):
        self.nb_articles = 0
        self.articles = []
        self.mt_articles = 0
        
        