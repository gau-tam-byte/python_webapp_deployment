import unittest


from translator import englishtofrench, frenchtoenglish
class Testetf(unittest.TestCase):
    def test1 (self):
        self.assertNotEqual(englishtofrench("Hello"), "Bonjour")


class Testfte(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchtoenglish("bonjour comment"), "hello how")
    
unittest.main()