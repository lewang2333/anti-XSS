#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

class CountPage(object):

    number = 0

    def __init__(self, number=0):
        self.number = number

        pass

    def setNumber(self, number):
        self.number = number

        pass

    def getNumber(self):
        return self.number

    def incNumber(self):
        self.number += 1

        pass

    def toString(self):
        return 'number = ' + str(number)
