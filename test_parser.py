from stack import Stack
import unittest
from parser import pars_checker

class Parstest(unittest.TestCase):

    def testtrueParser1(self):
        expressions=("","()", "[]", "2[5x(6+4)]", "{}")
        for expression in expressions:
            self.assertTrue(pars_checker(expression), "l'expression %s est %s alors qu'elle devrait être %s"%(expression, pars_checker(expression), True ))

    def testfalseParser(self):
        expressions=(")(", "[2*x*(45+6])", "]]", "())", "}{")
        for expression in expressions:
            self.assertFalse(pars_checker(expression), "l'expression %s est %s alors qu'elle devrait être %s"%(expression, pars_checker(expression), False ))

        
        
if __name__ == '__main__':
    unittest.main()
