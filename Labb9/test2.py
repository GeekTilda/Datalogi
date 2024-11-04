import unittest
from main import * 

class SyntaxTest(unittest.TestCase):
    def testUnknownAtom(self):
        self.assertEqual(tester2("C(Xx4)5"), "Okänd atom vid radslutet 4)5")

    def testUnknownNum(self):
        self.assertEqual(tester2("C(OH4)C"), "Saknad siffra vid radslutet C")

    def testNoParenthesis(self):
        self.assertEqual(tester2("C(OH4C"), "Saknad högerparentes vid radslutet ")

    def testWrongGroupStart(self):
        self.assertEqual(tester2("H2O)Fe"), "Felaktig gruppstart vid radslutet )Fe")

        self.assertEqual(tester2("(Cl)2)3"), "Felaktig gruppstart vid radslutet )3")
        self.assertEqual(tester2(")"), "Felaktig gruppstart vid radslutet )")
        self.assertEqual(tester2("2"), "Felaktig gruppstart vid radslutet 2")

    def testTooLittleNum(self):
        self.assertEqual(tester2("H0"), "För litet tal vid radslutet ")
        self.assertEqual(tester2("H1C"), "För litet tal vid radslutet C")
        self.assertEqual(tester2("H02C"), "För litet tal vid radslutet 2C")

    def testNoBigLetter(self):
        self.assertEqual(tester2("Nacl"), "Saknad stor bokstav vid radslutet cl")
        self.assertEqual(tester2("a"), "Saknad stor bokstav vid radslutet a")

if __name__ == "__main__":
    unittest.main()