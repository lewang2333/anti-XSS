#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

class Page(object):
    '''
    A class to store the page
    '''

    url = ''
    html = ''

    def __init__(self, url='', html=''):
        self.url = url
        self.html = html

        pass

    def get_html(self):
        return self.html
