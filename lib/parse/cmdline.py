#coding:utf8

import sys

from lib.core.engine import getPage
from lib.core.engine import links
from lib.core.link import Link
from optparse import OptionParser

def cmdLineParser():
    '''
    控制台
    '''
    parser = OptionParser()
    parser.add_option('-u', '--url', dest='startUrl', help='Target URL (e.g. \'http://www.site.com/\')')
    parser.add_option('-d', '--depth', dest='depth', help='The depth you want to scan (default: 10)')

    (options, args) = parser.parse_args()

    try:
        rootLink = Link(options.startUrl, options.startUrl)
        if options.depth:
            getPage(rootLink, int(options.depth))
        else:
            getPage(rootLink, 10)
    except Exception as e:
        print e
