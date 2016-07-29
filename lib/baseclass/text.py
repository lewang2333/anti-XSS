#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

class Text(object):
    '''
    Text is a base class that contains a text list.
    '''

    text = []

    def __init__(self):
        pass

    def toString(self):
        pass

    def setText(self, text):
        self.text = text

    def addTextLine(self, textLine):
        self.text.append(textLine)

    def getText(self):
        return self.text

    def getTextLine(self, index):
        return self.text[index]

    def getLength(self):
        return len(self.text)

    def delete(self, index):
        del self.text[index]

    def isIn(self, textLine):
        return textLine in self.text
