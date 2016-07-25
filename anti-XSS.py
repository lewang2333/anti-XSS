#coding: utf8

from getLink import *
from getPage import *
from findScript import *
from xssScanner import *

def main():
    domain = 'https://www.btcc.com'


    xssScanner(findScript(getPage('https://www.btcc.com/news'),domain))

if __name__ == '__main__':
    main()
