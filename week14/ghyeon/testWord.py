import unittest

from word import Word


class TestWord(unittest.TestCase):

    def setup(self):
        pass

    def tearDown(self):
        pass

    def testCount(self):
        self.g1 = Word("words.txt")
        t = self.g1.count
        self.assertEqual(t, 19184)

    def testTable(self):
        self.g1 = Word("words.txt")
        self.assertEqual(self.g1.table(), "default")

    def testRandfromDB(self):
        self.g1 = Word("words.txt")
        tmp = self.g1.randFromDB()
        self.assertEqual(tmp in self.g1.words, True)

if __name__ == '__main__':
    unittest.main()

