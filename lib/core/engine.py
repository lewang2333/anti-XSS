#coding: utf8
import os
import urllib
import urllib2

from script import Script
from lib.core.countpage import CountPage
from lib.core.link import Link

# 网页个数
countPage = CountPage(0)
# 所有扫描到的链接
links = []
# TODO: 把domain定义成全局变量
domain = 'https://www.btcc.com'
# 所有的js脚本
payloads = []
# 所有的XSS威胁
result = []

def createFile(countPage):
    fileName = 'temp/' + str(countPage)
    return fileName

def alreadyExist(link):
    for iLink in links:
        if link.getUrl() == iLink.getUrl():
            return True
    # if link in links:
    #     return True
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
def getPage(rootLink):
    global countPage
    # 如果没有temp目录就建立
    if not os.path.exists('temp/'):
        os.mkdir(r'temp/')
    # 把根域名加进队列
    links.append(rootLink)
    # 先得到根域名的html文件
    for link in links:
        countPage.incNumber()
        if countPage.getNumber() == 3:
            return
        urlRequest = urllib2.Request(link.getUrl())
        urlResponse = urllib2.urlopen(urlRequest)

        # 把html源码写入文件中
        # fileName = createFile(countPage.getNumber())
        # outputFile = open(fileName, 'w')
        # outputFile.write(htmlSource)
        # outputFile.close()
        # 写入完成

        # 把html源码写进Link类的__page中
        link.setPage(urlResponse.read())
        # 写入完成


        # 获取page中的链接
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
                # 格式化链接
                newUrl = formalizeLink(newUrl)
                # 链接补全
                newUrl = completeLink(newUrl, link.getUrl(), link.getDomain())
                # 构造新的link
                newLink = Link(newUrl, link.getDomain())
                if isLink(newLink.getUrl()) and (not alreadyExist(newLink)):
                     links.append(newLink)
            pointer = tailPos + 1

def getScript():
    global payloads
    global countPage
    # 调试代码
    countPage = 10
    for i in range(0, countPage - 1):
        fileName = 'temp/' + str(i + 1)
        inputFile = open(fileName, 'r')
        source = inputFile.read()

        head = 0
        length = len(source)
        flag = True
        while ((flag) and (head < length)):
            flag = False
            pos1 = source[head:].find('<script') + head
            pos2 = source[head:].find('</script>') + head
            if (pos1 >= head)and(pos2 >= head):
                flag = True
                tempString = source[pos1:pos2 + 9]
                tempString = tempString.replace('\t','')
                tempString = tempString.replace('\n','')
                tempString = tempString.replace(' ','')
                payload = Script(tempString)
                payloads.append(payload)
                head = pos2 + 10
        inputFile.close()
    for payload in payloads:
        print payload.getPayload()

def xssScanner():
    global payloads
    global result

    for payload in payloads:
        if (payload.find('cookie') > -1):
            payload.setDanger(True)
            result.append(payload)

    f2 = open('temp/result.md','w')
    f2.write('# XSS Scan Result\n')
    f2.write('## Found XSS Vulnerability\n```javascript\n')
    for i in result:
        f2.write(i.getPayload())
    f2.write('```\n')
    f2.close()


# 单元测试
if __name__ == '__main__':
    # if not os.path.exists('temp/'):
    #     os.mkdir(r'temp/')
    # getPage('https://www.btcc.com/news')
    getScript()
    xssScanner()
