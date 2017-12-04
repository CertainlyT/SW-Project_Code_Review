import unittest

from guess import Guess


class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess("aaaaaaaa")

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.g1.guess("e")
        self.g1.guess("n")
        self.assertEqual(self.g1.displayGuessed(), 'e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), 'a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), 'a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), 'a e n t u ')

    def testDisplayCurrent2(self):
        self.g2.guess("bbb")
        self.assertEqual(self.g2.displayCurrent(), "_ _ _ _ _ _ _ _ ")
        self.g2.guess(":")
        self.assertEqual(self.g2.displayCurrent(), "_ _ _ _ _ _ _ _ ")
        self.g2.guess("a")
        self.assertEqual(self.g2.displayCurrent(), "a a a a a a a a ")

    def testDisplayGuessed2(self):
        self.g2.guess("b")
        self.assertEqual(self.g2.displayGuessed(), "b ")
        self.g2.guess(":")
        self.assertEqual(self.g2.displayGuessed(), "b ")
        self.g2.guess("a")
        self.assertEqual(self.g2.displayGuessed(), "a b ")

    def testFinished(self):
        self.g1.guess("e")
        self.assertEqual(self.g1.finished(), False)
        self.assertEqual(self.g2.finished(), False)
        self.g2.guess("a")
        self.assertEqual(self.g2.finished(), True)


if __name__ == '__main__':
    unittest.main()
