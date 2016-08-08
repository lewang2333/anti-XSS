#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

import os
import datetime
import subprocess

from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

class PdfGnerator(object):
    # TODO: change the class name since there's a wrong spelling
    '''
    To generate the PDF report.
    '''
    __target = ''
    __text = []
    __pdfName = ''
    __path = 'result/'

    def __init__(self, text=[], target='your website', pdfName='Report.pdf'):
        self.__target = target
        self.__pdfName = self.__path + pdfName
        self.__text = text
        if not os.path.exists('result/'):
            os.mkdir(r'result/')
        time = datetime.datetime.today()
        date = time.strftime("%h-%d-%Y %H:%M:%S")
        c = canvas.Canvas(self.__pdfName)
        c.setPageSize((16 * inch,22 * inch))
        textobj = c.beginText()
        textobj.setTextOrigin(inch, 20 * inch)
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
