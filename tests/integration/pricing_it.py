import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from shop.pricing import final_price_cents


class TestPricingScenarios(unittest.TestCase):

    def test_bulk_order_scenario(self):
        items = [
            final_price_cents(500, discount_percent=10, tax_percent=20),
            final_price_cents(300, discount_percent=5, tax_percent=20),
            final_price_cents(200, discount_percent=0, tax_percent=20),
        ]
        total = sum(items)
        self.assertEqual(total, 540 + 342 + 240)

    def test_loyalty_discount_chain(self):
        base = 1000
        step1 = final_price_cents(base, discount_percent=20, tax_percent=0)
        step2 = final_price_cents(step1, discount_percent=10, tax_percent=0)
        self.assertEqual(step1, 800)
        self.assertEqual(step2, 720)

    def test_free_item_after_full_discount(self):
        price = final_price_cents(9999, discount_percent=100, tax_percent=20)
        self.assertEqual(price, 0)


if __name__ == "__main__":
    unittest.main()
