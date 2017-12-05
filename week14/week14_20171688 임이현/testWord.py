import unittest

from word import Word

class TestWord(unittest.TestCase):

    def setUp(self):
        self.w = Word('words.txt')

    def tearDown(self):
        pass

    def testTest(self):
        self.assertEqual(self.w.test(), 'default')

    def testrandFromDB(self):
        self.assertIn(self.w.randFromDB(), self.w.words)
        self.assertIn(self.w.randFromDB(), self.w.words)
        self.assertIn(self.w.randFromDB(), self.w.words)
        self.assertIn(self.w.randFromDB(), self.w.words)


if __name__ == '__main__':
    unittest.main()