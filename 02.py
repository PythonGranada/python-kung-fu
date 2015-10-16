#! /usr/bin/env python

from __future__ import print_function

# Author: Victor Terron (c) 2015
# Email: `echo vt2rron1iaa32s | tr 132 @.e`
# License: GNU GPLv3

""" Write a function that, given a list of integers, returns the product of
all the elements. You are not allowed to use neither a for nor a while loop. """

import unittest

def product(numbers):
    pass # place magic here

class ProductTests(unittest.TestCase):

    def test_product(self):
        self.assertEqual(     0, product([]))
        self.assertEqual(     0, product([0]))
        self.assertEqual(     1, product([1]))
        self.assertEqual(     5, product([5, 1]))
        self.assertEqual(    -6, product([3, -2]))
        self.assertEqual(     6, product([-3, -2]))
        self.assertEqual(    30, product([2, 3, 5]))
        self.assertEqual(362880, product(range(1, 10)))

if __name__ == "__main__":
    unittest.main()
