from stack import Stack
import unittest
from parser import pars_checker

class Parstest(unittest.TestCase):

    def testParser1(self):
        expression=""
        self.assertTrue(pars_checker(expression), "l'expression est s% alors qu'elle devrait être %s"%(pars_checker(expression), True ))
    
    def testParser2(self):
        expression="()"
        self.assertTrue(pars_checker(expression), "l'expression est s% alors qu'elle devrait être %s"%(pars_checker(expression), True ))
        
    def testParser3(self):
        expression=")("
        self.assertFalse(pars_checker(expression), "l'expression est s% alors qu'elle devrait être %s"%(pars_checker(expression), False ))
    
    def testParser4(self):
        expression="[2*x*(45+6])"
        self.assertFalse(pars_checker(expression), "l'expression est s% alors qu'elle devrait être %s"%(pars_checker(expression), False ))
     
    def testParser5(self):
        expression="())"
        self.assertFalse(pars_checker(expression), "l'expression est s% alors qu'elle devrait être %s"%(pars_checker(expression), True ))


        
        
if __name__ == '__main__':
    unittest.main()
