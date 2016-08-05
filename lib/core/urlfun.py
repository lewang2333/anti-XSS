#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

from lib.var.link import Link
from lib.var.links import Links
from lib.generator.linkfilter import LinkFilter


def formalize(url):
    '''
    Formalize the link (url)
    '''

    length = len(url)
    if url[length - 1] == '/':
        return url[:length - 1]

    return url


def isExist(url):
    '''
    Judge if the link is already exist in links[]
    '''

    for link in Links().getContent():
        if url.getUrl() == link.getUrl():
            return True

    return False


def initialize(url):
    if (url.find('http://') == -1) and (url.find('https://') == -1):
        return 'http://' + url

    return url


def isLink(url):
    # TODO: There may meet a problem when there is a couple of same keywords in the url;
    '''
    Judge if this link is a 'legel' link in scanner
    '''

    filterList = LinkFilter().getLinkFilter()
    for filterString in filterList:
        if url.find(filterString) != -1:
            return False

    return True
