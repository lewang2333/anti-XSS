#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

class ScriptTag(object):
    """docstring for """
    __list = []

    def __init__(self):
        try:
            f = open('lib/payload/scripttag.dic', 'r')
            payload = f.readline()
            while payload != '':
                self.__list.append(payload)
                payload = f.readline()

            f.close()
        except Exception as e:
            print ('''
Error: No script tag file in lib/payload/scripttag.dic
You should put your own tag file in lib/payload/
            ''')
            exit()

    def getScriptTag(self):
        return self.__list
