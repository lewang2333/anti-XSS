#!/usr/bin/env python

"""
Copyright (c) 2016 anti-XSS developers (http://laiw3n.com/)
"""

class ReportText(object):
    """docstring for """
    text = []

    def __init__(self, text=[]):
        pass

    def addText(self, text):
        self.text.append(text)

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text
