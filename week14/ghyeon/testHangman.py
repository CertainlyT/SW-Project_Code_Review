import unittest

from hangman import Hangman


class TestHangman(unittest.TestCase):

    def setup(self):
        pass

    def tearDown(self):
        pass

    def testDecreaseLife(self):
        self.g1 = Hangman()
        self.assertEqual(self.g1.remainingLives, 6)
        self.g1.decreaseLife()
        self.assertEqual(self.g1.remainingLives, 5)

    def testCurrentShape(self):
        self.g1 = Hangman()
        self.assertEqual(self.g1.currentShape(), self.g1.text[6])
        self.g1.decreaseLife()
        self.g1.decreaseLife()
        self.assertEqual(self.g1.currentShape(), self.g1.text[4])


if __name__ == "__main__":
    unittest.main()