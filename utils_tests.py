import unittest
from utils import Utils

class TestUtils(unittest.TestCase):

    def test_reversed(self):
        self.assertEqual(Utils.reversed(123), 321)
        self.assertEqual(Utils.reversed(3.14159), 951.14159)
        self.assertEqual(Utils.reversed("hello"), "olleh")

    def test_formatter(self):
        self.assertEqual(Utils.formatter(42), {"binary": "101010", "octal": "52"})
        self.assertEqual(Utils.formatter(7.5), {"binary": "111.1", "octal": "7.4"})
        self.assertEqual(Utils.formatter("abc"), {"binary": "110000110110001011010011", "octal": "30306123"})

if __name__ == '__main__':
    unittest.main()
