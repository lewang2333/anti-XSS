#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

import os
import urllib
import urllib2

from script import Script
from lib.core.link import Link
from lib.var.links import Links
from lib.var.scripts import Scripts
from lib.core.countpage import CountPage
from lib.generator.report import gnrReport
from lib.generator.scripttag import ScriptTag
from lib.generator.linkfilter import LinkFilter
from lib.generator.xsspayload import XssPayload
from lib.generator.pdfgenerator import PdfGnerator
from lib.structure.reporttext import ReportText

# print LinkFilter().getLinkFilter()

# TODO: Remove these vars or change it to class LE.WANG
# All JavaScript
scripts = []
# All XSS vulnerability payloads
xssScripts = []

def alreadyExist(link):
    '''
    Judge if the link is already exist in links[]
    '''
    for iLink in Links().getContent():
        if link.getUrl() == iLink.getUrl():
            return True

    return False

def getFatherUrl(url):
    # TODO: change this silly name of this function LE.WANG
    '''
    Return the upper link of url
    '''
    fatherUrl = url[::-1]
    pos = len(fatherUrl) - fatherUrl.find('/') + -1
    fatherUrl = fatherUrl[::-1][:pos]

    return fatherUrl

def isLink(link):
    # TODO: There may meet a problem when there is a couple of same keywords in the url;
    '''
    Judge if this link is a 'legel' link in scanner
    '''
    filterList = LinkFilter().getLinkFilter()
    for filterString in filterList:
        if link.find(filterString) != -1:
            return False

    return True

def formalizeLink(link):
    '''
    Formalize the link (url)
    '''
    formalizedLink = link
    formalizedLink = formalizedLink.replace('\t','')
    formalizedLink = formalizedLink.replace('\n','')
    formalizedLink = formalizedLink.replace(' ','')
    if formalizedLink[len(formalizedLink) - 1] == '/':
        formalizedLink = formalizedLink[:len(formalizedLink) - 1]
        # print formalizedLink
    return formalizedLink

def getRoot(url):
    '''
    Return the domain
    '''
    pos = url[8:].find('/')
    if pos == -1:
        return url
    rootUrl = url[:pos + 8]
    return rootUrl

def completeLink(link, hostUrl, domain):
    completedLink = link
    if completedLink == '':
        return hostUrl
    if completedLink.find('[[site]]') != -1:
        completedLink = completedLink.replace('[[site]]',domain)
    elif (completedLink.find('http') == -1):
        if (completedLink[0] == '?'):
            completedLink = hostUrl + completedLink
        elif (completedLink[0] != '/'):
            completedLink = hostUrl + '/' + completedLink
        else:
            completedLink = getRoot(hostUrl) + completedLink
            # print completedLink
    return completedLink


def getPage(rootLink, depth):
    # Init the glbal var CountPage().number as 0
    CountPage(0)

    Links().addText(rootLink)
    # Download the source file of root link and set it as the root in BFS queue
    for link in Links().getContent():
        CountPage().incNumber()
        if CountPage().getNumber() == depth:
            return
        urlRequest = urllib2.Request(link.getUrl())
        urlResponse = urllib2.urlopen(urlRequest)
        link.setPage(urlResponse.read())

        # A humble way to insert links into queue
        # TODO: Threads mode
        htmlSource = link.getPage().lower()
        pointer = 0
        pageLength = len(htmlSource)
        isAnyScript = True
        while (isAnyScript) and (pointer < pageLength):
            flag = False
            headPos = htmlSource[pointer:].find('href="') + pointer
            tailPos = htmlSource[headPos + 7:].find('"') + headPos + 7
            if (headPos >= pointer) and (tailPos >= pointer):
                isAnyScript = True
                newUrl = htmlSource[headPos + 6:tailPos]
                # print newUrl
                # Formalize the origin link
                newUrl = formalizeLink(newUrl)
                # Complete it with domain
                newUrl = completeLink(newUrl, link.getUrl(), link.getDomain())
                # Reconstruct link
                newLink = Link(newUrl, link.getDomain())
                if isLink(newLink.getUrl()) and (not alreadyExist(newLink)):
                     Links().addText(newLink)
                    #  print newLink.getUrl()
            pointer = tailPos + 1

def getScript():
    # global scripts

    scriptTags = ScriptTag().getScriptTag()

    for link in Links().getContent():
        for scriptTag in scriptTags:
            headTag = scriptTag.replace('\n','').split('|')[0]
            tailTag = scriptTag.replace('\n','').split('|')[1]
            source = link.getPage()
            head = 0
            length = len(source)
            flag = True
            while ((flag) and (head < length)):
                flag = False
                pos1 = source[head:].find(headTag) + head
                pos2 = source[head:].find(tailTag) + head
                if (pos1 >= head)and(pos2 >= head):
                    flag = True
                    tempString = source[pos1:pos2 + 9]
                    tempString = tempString.replace('\t','')
                    tempString = tempString.replace('\n','')
                    tempString = tempString.replace(' ','')
                    script = Script(tempString, link.getUrl())
                    Scripts().addText(script)
                    # scripts.append(script)
                    head = pos2 + 10



def xssScanner():
    # global scripts
    global xssScripts

    xssPayloads = XssPayload().getXssPayload()

    # for script in scripts:
    for script in Scripts().getContent():
        for xssPayload in xssPayloads:
            if (script.getScript().find(xssPayload.replace('\n','')) > -1):
                script.setDanger(True)
                xssScripts.append(script.getScript() + '\t' + script.getFromDomain())

                break

    gnrReport(xssScripts)
    PdfGnerator(ReportText().getText())
