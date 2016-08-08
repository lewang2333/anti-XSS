#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

import sys
import os

from lib.var.reporttext import ReportText

def gnrReport(xssScripts):

    ReportText().addText('')
    ReportText().addText('Summary')
    ReportText().addText('There are ' + str(len(xssScripts)) + ' XSS vulnerabilities found.\n\n')
    if len(xssScripts) < 1:
        return None
    ReportText().addText('')
    ReportText().addText('Found vulnerabilities')
    for xssScript in xssScripts:
        head = xssScript.split('\t')[0]
        tail = xssScript.split('\t')[1]
        ReportText().addText('Payload: ' + head)
        ReportText().addText('From: ' + tail)
        ReportText().addText('')
