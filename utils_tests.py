
import unittest
from utils import utils

class TestUtils(unittest.TestCase):

    def test_reversed_with_integers(self):
        self.assertEqual(utils.reversed(12345), 54321)
        self.assertEqual(utils.reversed(987654321), 123456789)

    def test_reversed_with_strings(self):
        with self.assertRaises(ValueError):
            utils.reversed("12345")
        with self.assertRaises(ValueError):
            utils.reversed("987654321")

    def test_reversed_with_floats(self):
        with self.assertRaises(ValueError):
            utils.reversed(12.34)

    def test_formatter_with_integers(self):
        self.assertEqual(utils.formatter(10), ('1010', '12'))
        self.assertEqual(utils.formatter(42), ('101010', '52'))

    def test_formatter_with_strings(self):
        with self.assertRaises(ValueError):
            utils.formatter("42")

    def test_formatter_with_floats(self):
        with self.assertRaises(ValueError):
            utils.formatter(12.34)

if __name__ == '__main__':
    unittest.main()
