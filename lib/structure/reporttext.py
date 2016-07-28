#!/usr/bin/env python

"""
Copyright (c) 2016 anti-XSS developers (http://laiw3n.com/)
"""

class ReportText(object):
    """docstring for """
    text = []

    def addText(self, text):
        ReportText.text.append(text)

    def setText(self, text):
        ReportText.text = text

    def getText(self):
        return ReportText.text
