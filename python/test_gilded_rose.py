# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose
from python.config import MIN_QUALITY, MAX_QUALITY, NORMAL, BRIE, SULFURAS, BACKSTAGE


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    import unittest


class TestGildedRose(unittest.TestCase):
    def test_normal_item_quality_decreases_by_one(self):
        items = [Item(NORMAL, 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].quality)

    # As it is an operation that is performed independently of the type of item, it is considered that one test case
    # is sufficient.
    def test_item_sell_in_decreases_by_one(self):
        items = [Item(NORMAL, 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)

    def test_normal_item_quality_decreases_by_two_after_sell_in_date(self):
        items = [Item(NORMAL, 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8, items[0].quality)

    def test_normal_item_quality_never_negative(self):
        items = [Item(NORMAL, 5, MIN_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_quality_increases_by_one(self):
        items = [Item(BRIE, 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)

    def test_aged_brie_quality_increases_by_two_after_sell_in_date(self):
        items = [Item(BRIE, 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)

    def test_aged_brie_quality_never_above_50(self):
        items = [Item(BRIE, 5, MAX_QUALITY)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)

    def test_aged_brie_quality_increases_by_one_before_sell_in_date(self):
        items = [Item(BRIE, 5, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(41, items[0].quality)

    def test_sulfuras_quality_never_changes(self):
        items = [Item(SULFURAS, 5, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(40, items[0].quality)

    def test_sulfuras_sell_in_never_changes(self):
        items = [Item(SULFURAS, 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].sell_in)

    def test_backstage_pass_quality_decreases_to_zero_after_sell_in_date(self):
        items = [Item(BACKSTAGE, 0, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_backstage_pass_quality_increases_by_one_when_sell_in_greater_than_10(self):
        items = [Item(BACKSTAGE, 11, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(11, items[0].quality)

    def test_backstage_pass_quality_increases_by_two_when_sell_in_less_than_or_equal_to_10(self):
        items = [Item(BACKSTAGE, 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(12, items[0].quality)

    def test_backstage_pass_quality_increases_by_three_when_sell_in_less_than_or_equal_to_5(self):
        items = [Item(BACKSTAGE, 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(13, items[0].quality)


if __name__ == '__main__':
    unittest.main()
