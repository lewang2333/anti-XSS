#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

class Links(object):
    '''
    Links class used as a global var.
    '''

    content = []

    def __init__(self):
        pass

    def addText(self, text):
        self.content.append(text)

    def setText(self, content):
        self.content = content

    def getText(self):
        return self.content
