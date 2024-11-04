import unittest
from main import * 

class SyntaxTest(unittest.TestCase):
    def testCorrMol(self):
        self.assertEqual(tester1("Na"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(tester1("H2O"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(tester1("Si(C3(COOH)2)4(H2O)7"), "Formeln är syntaktiskt korrekt")
        self.assertEqual(tester1("Na332"), "Formeln är syntaktiskt korrekt")

if __name__ == "__main__":
    unittest.main()