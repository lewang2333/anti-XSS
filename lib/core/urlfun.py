#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

def formalize(url):
    '''
    Formalize the link (url)
    '''

    length = len(url)
    if url[length - 1] == '/':
        return url[:length - 1]

    return url
