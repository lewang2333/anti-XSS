#!/usr/bin/env python

"""
Copyright (c) 2016 anti-XSS developers (http://laiw3n.com/)
"""

import sys
import os

from lib.structure.reporttext import ReportText

def gnrReport(xssScripts):

    ReportText().addText('')
    ReportText().addText('Summary')
    ReportText().addText('There are ' + str(len(xssScripts)) + ' XSS vulnerabilities found.\n\n')
    if len(xssScripts) < 1:
        return None
    ReportText().addText('')
    ReportText().addText('Found vulnerabilities')
    for xssScript in xssScripts:
        ReportText().addText('Payload: ' + xssScript.getScript() + '\t From: ' + xssScript.getFromDomain() + '\n\n')
