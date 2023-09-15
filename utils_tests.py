import unittest
from utils import Utils

class Test_Utils(unittest.TestCase):

    def test_reversed(self):
        self.assertEqual(Utils.reversed(123), 321)
        self.assertEqual(Utils.reversed(556), 655)
        with self.assertRaises(TypeError):
            Utils.reversed("abc")  

    def test_formatter(self):
        self.assertEqual(Utils.formatter(42), {"binary": "101010", "octal": "0o52"})
        self.assertEqual(Utils.formatter(7), {"binary": "111", "octal": "0o7"})
        with self.assertRaises(TypeError):
            Utils.formatter(7.5)  
        with self.assertRaises(TypeError):
            Utils.formatter("abc")  
if __name__ == '__main__':
    unittest.main()
