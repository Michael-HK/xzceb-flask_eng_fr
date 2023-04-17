import unittest
import translator

class TestMethod(unittest.TestCase):
    def test_1(self):
        self.assertIsNotNone(translator.english_to_french('Hello'))
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')

    def test_2(self):
        self.assertIsNotNone(translator.french_to_english('Bonjour'))
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()