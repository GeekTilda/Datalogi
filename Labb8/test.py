import unittest

def LETTER(char):
    return 'A' <= char <= 'Z'

class TestLETTERFunc(unittest.TestCase):
    def testLETTER1(self):
        self.assertEqual(LETTER("A"), True)

    def testLETTERWrong(self):
        self.assertEqual(LETTER("b"), True)

    def testLETTER2(self):
        self.assertEqual(LETTER("G"), True)

    def testLETTER3(self):
        self.assertEqual(LETTER("Z"), True)


unittest.main()