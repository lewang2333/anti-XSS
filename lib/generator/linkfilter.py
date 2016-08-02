#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

class LinkFilter(object):
    """docstring for """
    __list = []

    def __init__(self):
        try:
            f = open('lib/payload/linkfilter.dic', 'r')
            payload = f.readline()
            while payload != '':
                self.__list.append(payload.replace('\n',''))
                payload = f.readline()

            f.close()
        except Exception as e:
            print ('''
Error: No link filter file in lib/payload/linkfilter.dic
You should put your own filter file in lib/payload/
            ''')
            exit()

    def getLinkFilter(self):
        return self.__list
