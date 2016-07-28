#!/usr/bin/env python

"""
Copyright (c) 2016 anti-XSS developers (http://laiw3n.com/)
"""

import sys
import os


def gnrReport(xssScripts):

    fileName = 'result/report.md'

    if not os.path.exists('result/'):
        os.mkdir(r'result/')

    f = open(fileName, 'w')

    f.write('# anti-XSS Cross Site Script Scanning Report\n\n')
    f.write('## Summary\n\n')
    f.write('There are ' + str(len(xssScripts)) + ' XSS vulnerabilities found.\n\n' )

    if len(xssScripts) < 1:
        return None

    f.write('## Found vulnerabilities \n\n')

    for xssScript in xssScripts:
        f.write('Payload: ' + xssScript.getScript() + '\t From: ' + xssScript.getFromDomain() + '\n\n')

    f.close()
