#coding: utf8
import sys
import os


def gnrReport(xssScripts):
    '''
    明天要把xssScripts写成一个类！
    '''

    fileName = 'result/report.md'

    if not os.path.exists('result/'):
        os.mkdir(r'result/')

    f = open(fileName, 'w')

    f.write('# anti-XSS Cross Site Script Scanning Report\n')
    f.write('## Summary\n')
    f.write('There are ' + str(len(xssScripts)) + ' XSS vulnerabilities found.\n' )

    if len(xssScripts) < 1:
        return None

    f.write('## Found vulnerabilities \n')

    for xssScript in xssScripts:
        f.write('Payload: ' + xssScript.getScript() + '\t From: ' + xssScript.getFromDomain() + '\n')

    f.close()
