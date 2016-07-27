#coding: utf8
import os
import urllib
import urllib2

# 网页个数
countPage = 0
# 所有扫描到的链接
links = []
# TODO: 把domain定义成全局变量
domain = 'https://www.btcc.com'

def createFile(countPage):
    fileName = 'temp/' + str(countPage)
    return fileName

def alreadyExist(link):
    if link in links:
        return True
    return False

def getFatherUrl(url):
    fatherUrl = url[::-1]
    pos = len(fatherUrl) - fatherUrl.find('/') + -1
    fatherUrl = fatherUrl[::-1][:pos]
    return fatherUrl

def isLink(link):
    if (link.find('page') > -1):
        pos = link.find('page')
        if (link[pos+1:].find('page') > -1):
            return False
    if (link.find('javascript') > -1):
        return False
    if (link.find('google') > -1):
        return False
    if (link.find('twitter') > -1):
        return False
    if (link.find('help?') > -1):
        return False
    if (link.find('btcc') > -1) and (link.find('.png') == -1) and (link.find('.css') == -1) and (link.find('forg') == -1):
        return True
    return False

def formalizeLink(link):
    formalizedLink = link
    formalizedLink = formalizedLink.replace('\t','')
    formalizedLink = formalizedLink.replace('\n','')
    formalizedLink = formalizedLink.replace(' ','')
    if formalizedLink[len(formalizedLink) - 1] == '/':
        formalizedLink = formalizedLink[:len(formalizedLink) - 1]
    return formalizedLink

def getRoot(url):
    pos = url[8:].find('/')
    if pos == -1:
        return url
    rootUrl = url[:pos + 8]
    return rootUrl

def completeLink(link, hostUrl, domain):
    completedLink = link
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
            # print hostUrl
    return completedLink


# 传入一个list文件，包含所有等根域名
def getPage(urlList):
    global countPage
    # 把根域名加进队列
    links.append(urlList)
    # 先得到根域名的html文件
    for hostUrl in links:
        countPage = countPage + 1
        # print 'This is the times: ' + str(countPage)
        if countPage == 10:
            # for i in links:
            #     print i
            return
        urlRequest = urllib2.Request(hostUrl)
        urlResponse = urllib2.urlopen(urlRequest)
        htmlSource = urlResponse.read()
        # 把html源码写入文件中
        fileName = createFile(countPage)
        outputFile = open(fileName, 'w')
        outputFile.write(htmlSource)
        outputFile.close()
        # 写入完成

        # 获取page中的链接
        htmlSource = htmlSource.lower()
        pointer = 0
        pageLength = len(htmlSource)
        isAnyScript = True
        while (isAnyScript) and (pointer < pageLength):
            flag = False
            headPos = htmlSource[pointer:].find('href="') + pointer
            tailPos = htmlSource[headPos + 7:].find('"') + headPos + 7
            if (headPos >= pointer) and (tailPos >= pointer):
                isAnyScript = True
                link = htmlSource[headPos + 6:tailPos]
                # 格式化链接
                link = formalizeLink(link)
                # 链接补全
                link = completeLink(link, hostUrl, domain)
                if isLink(link) and (not alreadyExist(link)):
                     links.append(link)
                    #  print link
            pointer = tailPos + 1

# 单元测试
if __name__ == '__main__':
    if not os.path.exists('temp/'):
        os.mkdir(r'temp/')
    getPage('https://www.btcc.com/news')
    f = open('temp/links.txt','w')
    for i in links:
        f.write(i + '\n')
    f.close()
