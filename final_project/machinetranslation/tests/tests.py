import unittest

from translator import frenchToEnglish, englishToFrench

class TestMyModule(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(None), "null")
        self.assertEqual(englishToFrench("Hello"), "Bonjour")
    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(None), "null")
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

if __name__ == "__main__":
    unittest.main()