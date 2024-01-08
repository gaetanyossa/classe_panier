import unittest

class Panier:
    def __init__(self):
        self.articles = {}

    def ajouter_article(self, article, quantite=1, prix_unitaire=0.0):
        if article in self.articles:
            self.articles[article]['quantite'] += quantite
        else:
            self.articles[article] = {'quantite': quantite, 'prix_unitaire': prix_unitaire}

    def retirer_article(self, article, quantite=1):
        if article in self.articles:
            if self.articles[article]['quantite'] <= quantite:
                del self.articles[article]
            else:
                self.articles[article]['quantite'] -= quantite

    def calculer_total(self):
        total = 0.0
        for article, info in self.articles.items():
            total += info['quantite'] * info['prix_unitaire']
        return total

    def vider_panier(self):
        self.articles = {}

# Tests unitaires
class TestPanier(unittest.TestCase):
    def setUp(self):
        self.panier = Panier()

    def test_ajouter_article(self):
        self.panier.ajouter_article('Pomme', quantite=3, prix_unitaire=1.5)
        self.assertEqual(self.panier.articles['Pomme']['quantite'], 3)

    def test_retirer_article(self):
        self.panier.ajouter_article('Banane', quantite=2, prix_unitaire=0.8)
        self.panier.retirer_article('Banane', quantite=1)
        self.assertEqual(self.panier.articles.get('Banane', None), {'quantite': 1, 'prix_unitaire': 0.8})

    def test_calculer_total(self):
        self.panier.ajouter_article('Orange', quantite=4, prix_unitaire=1.2)
        self.panier.ajouter_article('Poire', quantite=2, prix_unitaire=2.0)
        self.assertEqual(self.panier.calculer_total(), 10.8)

    def test_vider_panier(self):
        self.panier.ajouter_article('Chocolat', quantite=1, prix_unitaire=3.5)
        self.panier.vider_panier()
        self.assertEqual(len(self.panier.articles), 0)

if __name__ == '__main__':
    unittest.main()
