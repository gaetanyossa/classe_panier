import unittest
from classe_panier import Article, Panier 

        
        
class TestMaClassePanier(unittest.TestCase):
    def setUp(self):
        # Initialisation des objets de test
        self.article1 = Article("Article 1", 30)
        self.article2 = Article("Article 2", 25)

        self.objet_classe = Panier()

    def test_ajouter_article(self):
        self.objet_classe.ajouter_article(self.article1)
        self.assertEqual(self.objet_classe.nb_articles, 1)
        self.assertEqual(self.objet_classe.mt_articles, 30)

    def test_retirer_article(self):
        self.objet_classe.ajouter_article(self.article1)
        self.objet_classe.ajouter_article(self.article2)

        self.objet_classe.retirer_article(self.article1)
        self.assertEqual(self.objet_classe.nb_articles, 1)
        self.assertEqual(self.objet_classe.mt_articles, 25)

    def test_retirer_article_inexistant(self):
        # Tentative de retirer un ami qui n'est pas dans la liste
        article_inexistant = Article("Article Inexistant", 40)
        self.objet_classe.retirer_article(article_inexistant)
        self.assertEqual(self.objet_classe.nb_articles, 0)
        self.assertEqual(self.objet_classe.mt_articles, 0)
        
    def test_vider_panier(self):
        self.objet_classe.ajouter_article(self.article1)
        self.objet_classe.ajouter_article(self.article2)
        
        self.objet_classe.vider_panier()
        
        self.assertEqual(self.objet_classe.nb_articles, 0)
        self.assertEqual(self.objet_classe.mt_articles, 0)

if __name__ == '__main__':
    unittest.main()