#!/usr/bin/env python

"""
Copyright (c) 2016 anti-XSS developers (http://laiw3n.com/)
"""

class CountPage(object):

    __number = 0

    def __init__(self, number=0):
        self.__number = number

    def setNumber(self, number):
        self.__number = number

    def getNumber(self):
        return self.__number

    def incNumber(self):
        self.__number += 1
