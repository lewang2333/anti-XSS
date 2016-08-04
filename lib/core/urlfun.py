#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

from lib.core.link import Link
from lib.var.links import Links

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
