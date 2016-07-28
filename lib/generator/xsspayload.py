#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

class XssPayload(object):
    """docstring for """
    __list = []

    def __init__(self):
        try:
            f = open('lib/payload/xsspayload.dic', 'r')
            payload = f.readline()
            while payload != '':
                self.__list.append(payload)
                payload = f.readline()

            f.close()
        except Exception as e:
            print ('''
Error: No XSS payload file in lib/payload/xsspayload.dic
You should put your own dictionary file in lib/payload/
            ''')
            exit()

    def getXssPayload(self):
        return self.__list
