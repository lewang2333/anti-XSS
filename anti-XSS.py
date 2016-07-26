#coding: utf8

from getLink import *
from getPage import *
from findScript import *
from xssScanner import *

def main():
    domain = 'https://staging.btcc.com'
    target = 'https://www.btcc.com/news'

    getLink(getPage(target),target)

    xssScanner(findScript(getPage('https://staging.btcc.com/news'),domain))

if __name__ == '__main__':
    main()
