#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

class Script(object):
    '''
    To store Javascript
    '''

    __script = ''
    __fromDomain = ''
    __danger = False

    def __init__(self, script='', fromDomain='', danger=False):
        self.__script = script
        self.__fromDomain = fromDomain
        self.__danger = danger

    def setScript(script):
        self.__script = script

    def setFromDomain(fromDomain):
        self.__fromDomain = fromDomain

    def setDanger(self, danger):
        self.__danger = danger

    def getScript(self):
        return self.__script

    def getFromDomain(self):
        return self.__fromDomain

    def getDanger(self):
        return self.__danger

    def find(self, target):
        return self.__script.find(target)

    def toString(self):
        return 'script= ' + self.__script + '\nfromDomain= ' + self.__fromDomain + '\ndanger= ' + str(self.__danger)
