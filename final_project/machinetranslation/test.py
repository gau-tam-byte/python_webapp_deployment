import unittest


from translator import englishtofrench, frenchtoenglish
class Testetf(unittest.TestCase):
    def test1 (self):
        self.assertNotEqual(englishtofrench("Hello"), "Bonjour")
        self.assertEqual(englishtofrench("Hi"), "Bonjour")


class Testfte(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchtoenglish("bonjour comment"), "hello how")
        self.assertNotEqual(frenchtoenglish("Salut"), "Hi")
    
if __name__ == "__main__":
    unittest.main()