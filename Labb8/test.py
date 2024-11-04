import unittest
from main import * 

class SyntaxTest(unittest.TestCase):
    def testCorrMol(self):
        self.assertEqual(tester("H2"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(tester("H2O"), "Formeln är syntaktiskt korrekt")

    def testWrongMol(self):
        self.assertEqual(tester("a"), "Saknad stor bokstav vid radslutet a")

    def testWrongMol2(self):
        self.assertEqual(tester("H01011"),"För litet tal vid radslutet 1011")

if __name__ == "__main__":
    unittest.main()