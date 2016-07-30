#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

class CountPage(object):

    number = 0

    def __init__(self, number=0):
        self.number = number

    def setNumber(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def incNumber(self):
        self.number += 1
