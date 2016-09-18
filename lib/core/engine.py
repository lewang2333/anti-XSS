#!/usr/bin/env python

'''
Copyright (c) 2016 anti-XSS developers
'''

import os
import urllib
import urllib2

from lib.core.urlfun import *

from script import Script
from lib.var.link import Link
from lib.var.links import Links
from lib.var.scripts import Scripts
from lib.var.countpage import CountPage
from lib.var.xssscripts import XssScripts
from lib.var.reporttext import ReportText
from lib.generator.report import gnrReport
from lib.generator.scripttag import ScriptTag
from lib.generator.xsspayload import XssPayload
from lib.generator.pdfgenerator import PdfGnerator
from lib.var.page import Page

def scan(target):

    newpage = Page(url=target, html=get_html(target))

    return newpage.get_html()

def get_html(url):
    '''
    Retrun the html code of the URL
    '''

    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()

    return html

def getFatherUrl(url):
    # TODO: change this silly name of this function LE.WANG
    '''
    Return the upper link of url
    '''

    fatherUrl = url[::-1]
    pos = len(fatherUrl) - fatherUrl.find('/') + -1
    fatherUrl = fatherUrl[::-1][:pos]

    return fatherUrl

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
    '''
    Complete the link url
    '''

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

    return completedLink

def getPage(rootLink, depth):
    '''
    Get the source code of pages and get the links on them
    '''

    # Init the glbal var CountPage().number with 0
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
                # Formalize the origin link
                newUrl = formalize(newUrl)
                # Complete it with domain
                newUrl = completeLink(newUrl, link.getUrl(), link.getDomain())
                # Reconstruct link
                newLink = Link(newUrl, link.getDomain())
                if isLink(newLink.getUrl()) and (not isExist(newLink)):
                     Links().addText(newLink)
            pointer = tailPos + 1

    pass

def getScript():
    '''
    Store the JavaScript
    '''

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
                    head = pos2 + 10

    pass

def xssScanner():
    '''
    Store the XSS Script
    '''

    xssPayloads = XssPayload().getXssPayload()

    for script in Scripts().getContent():
        for xssPayload in xssPayloads:
            if (script.getScript().find(xssPayload.replace('\n','')) > -1):
                script.setDanger(True)
                XssScripts().addText(script.getScript() + '\t' + script.getFromDomain())

                break

    gnrReport(XssScripts().getContent())
    PdfGnerator(ReportText().getText())

    pass
