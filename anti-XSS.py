#coding: utf8

import sys

from lib.parse.cmdline import cmdLineParser
from lib.core.engine import getPage
from lib.core.link import Link
from lib.core.engine import links

def main():
    '''
    main函数
    '''
    cmdLineParser()

    # 用传入的网址构造一个Link类
    rootLink = Link(sys.argv[1], sys.argv[1])

    getPage(rootLink)

    print len(links)
    for i in links:
        print i.getUrl()

if __name__ == '__main__':
    main()
