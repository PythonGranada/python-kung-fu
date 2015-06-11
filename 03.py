#! /usr/bin/env python

from __future__ import print_function

# Author: Victor Terron (c) 2015
# Email: `echo vt2rron1iaa32s | tr 132 @.e`
# License: GNU GPLv3

""" Write a function that tells us whether a string is a rotation of another.
You can make at most one call to the 'in' operator or to the methods index()
and find() """

def is_rotation(word, another):
    pass # place magic here

if __name__ == "__main__":

    sentence = "Hari Seldon"
    print(is_rotation(sentence, "ldonHari Se")) # True
    print(is_rotation(sentence, "Hari Hari H")) # False
