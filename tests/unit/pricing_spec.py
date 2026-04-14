import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from shop.pricing import final_price_cents


class TestFinalPrice(unittest.TestCase):

    def test_no_discount_no_tax(self):
        result = final_price_cents(1000, discount_percent=0, tax_percent=0)
        self.assertEqual(result, 1000)

    def test_default_tax_applied(self):
        result = final_price_cents(1000)
        self.assertEqual(result, 1200)

    def test_discount_50(self):
        result = final_price_cents(1000, discount_percent=50, tax_percent=0)
        self.assertEqual(result, 500)

    def test_discount_100(self):
        result = final_price_cents(500, discount_percent=100, tax_percent=20)
        self.assertEqual(result, 0)

    def test_discount_and_tax_combined(self):
        result = final_price_cents(1000, discount_percent=10, tax_percent=10)
        self.assertEqual(result, 990)

    def test_tax_100_percent(self):
        result = final_price_cents(200, discount_percent=0, tax_percent=100)
        self.assertEqual(result, 400)

    def test_invalid_base_negative(self):
        with self.assertRaises(ValueError):
            final_price_cents(-1, discount_percent=0, tax_percent=0)

    def test_invalid_discount_over_100(self):
        with self.assertRaises(ValueError):
            final_price_cents(100, discount_percent=150, tax_percent=0)

    def test_invalid_tax_negative(self):
        with self.assertRaises(ValueError):
            final_price_cents(100, discount_percent=0, tax_percent=-5)

    def test_invalid_type_none_base(self):
        with self.assertRaises(TypeError):
            final_price_cents(None, discount_percent=0, tax_percent=0)

    def test_invalid_type_str_discount(self):
        with self.assertRaises(TypeError):
            final_price_cents(100, discount_percent="10", tax_percent=0)

    def test_zero_base(self):
        result = final_price_cents(0, discount_percent=50, tax_percent=20)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
