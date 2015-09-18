#! /usr/bin/env python

from __future__ import print_function

# Author: Victor Terron (c) 2015
# Email: `echo vt2rron1iaa32s | tr 132 @.e`
# License: GNU GPLv3

""" Write a function that returns whether a string has all unique characters.
For extra points, do it without using any additional data structure (such as
lists or dictionaries). You can use any function in the standard library. """

import unittest

def all_unique(word):
    pass # place magic here

class AllUniqueTests(unittest.TestCase):

  def test_all_unique(self):

    self.assertTrue (all_unique(""))
    self.assertTrue (all_unique("a"))
    self.assertTrue (all_unique("B"))
    self.assertTrue (all_unique("abcde"))
    self.assertTrue (all_unique("aBcDe"))
    self.assertFalse(all_unique("aa"))    # Two a's
    self.assertFalse(all_unique("bB"))    # Two b's (in different cases)
    self.assertFalse(all_unique("abCdc")) # Two c's

if __name__ == "__main__":
    unittest.main()
