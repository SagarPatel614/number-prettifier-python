import unittest
from prettifier import LargeNumberPrettifier


class TestLargeNumberPrettifier(unittest.TestCase):
    def setUp(self):
        self.prettifier = LargeNumberPrettifier()

    def test_million(self):
        self.assertEqual(self.prettifier.prettify(1000000), "1M")

    def test_million_with_decimal(self):
        self.assertEqual(self.prettifier.prettify(2500000.34), "2.5M")

    def test_small_number(self):
        self.assertEqual(self.prettifier.prettify(532), "532")

    def test_billion(self):
        self.assertEqual(self.prettifier.prettify(1123456789), "1.1B")

    def test_trillion(self):
        self.assertEqual(self.prettifier.prettify(1500000000000), "1.5T")

    def test_number_below_million(self):
        self.assertEqual(self.prettifier.prettify(999999), "999999")

    def test_large_trillions(self):
        self.assertEqual(self.prettifier.prettify(10000000000000), "10T")


if __name__ == "__main__":
    unittest.main()
