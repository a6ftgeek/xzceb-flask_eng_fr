import unittest
from translator import english_to_french, french_to_english

class TestTranslations(unittest.TestCase):

    def test_e2f(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('Name'), 'Nom')

    def test_f2e(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Nom'), 'Name')

if __name__ == '__main__':
    unittest.main()
    