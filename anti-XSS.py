#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

import sys

from lib.core.urlfun import *

from lib.var.link import Link
from optparse import OptionParser
from lib.core.engine import getPage
from lib.core.engine import getScript
from lib.core.engine import xssScanner
from lib.generator.report import gnrReport

def main():
    parser = OptionParser()
    parser.add_option('-u', '--url', dest='startUrl', help='Target URL (e.g. \'http://www.site.com/\')')
    parser.add_option('-d', '--depth', dest='depth', help='The depth you want to scan (default: 2)')
    (options, args) = parser.parse_args()

    if options.startUrl:
        url = initialize(options.startUrl)
        rootLink = Link(url, url)
        if options.depth:
            getPage(rootLink, int(options.depth))
        else:
            getPage(rootLink, 2)
        getScript()
        xssScanner()

    pass

if __name__ == '__main__':
    main()
