import unittest
from convertisseur import calcul
class Convertest(unittest.TestCase):
    
    def testConver1(self): #on fait un test
        expressions=[("2","4","3","+","*","4","-"), ("5","4","+","2","9","*","4","-","+"), ("11", "45", "8", "6", "-", "+","+","2","^"), ("-2", "-4","+"), ("4.5","5","+")]
        resultats=(10, 23, 3364, -6, 9.5)
        for i in range(len(expressions)-1):
            self.assertEqual(calcul(expressions[i]), resultats[i]," l'expression %s est égale à %s, elle devrait être égale à %s"%(expressions[i],calcul(expressions[i]), resultats[i]))
            
if __name__ == '__main__':
    unittest.main()


