#!/usr/bin/env python

"""
Copyright (c) 2016 anti-XSS developers (http://laiw3n.com/)
"""

import datetime
import subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

class PdfReport(object):
    """docstring for """
    __target = ''
    __text = []
    __pdfName = ''
    __path = '../../result/'

    def __init__(self, target='your website', pdfName='Report.pdf', text=[]):
        self.__target = target
        self.__pdfName = self.__path + pdfName
        self.__text = text
        time = datetime.datetime.today()
        date = time.strftime("%h-%d-%Y %H:%M:%S")
        c = canvas.Canvas(self.__pdfName)
        textobj = c.beginText()
        textobj.setTextOrigin(inch, 11 * inch)
        textobj.textLines('''
            This is the scanning report of %s.
            ''' %self.__target)
        textobj.textLines('''
            Date: %s
            ''' % date)
        for line in self.__text:
            textobj.textLine(line.strip())
        c.drawText(textobj)
        c.showPage()
        c.save()

    def setText(self, text):
        self.__text = text

    def getText(self):
        return self.__text

    def setPdfName(self, pdfName):
        self.__pdfName = pdfName

    def getText(self):
        return self.__pdfName
