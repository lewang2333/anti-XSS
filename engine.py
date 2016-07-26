#coding: utf8
import os
import urllib
import urllib2

# 网页个数
countPage = 0
# 所有扫描到的链接
links = []
# TODO: 把domain定义成全局变量
domain = 'https://www.btcc.com/news'

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
    if (link.find('btcc') > -1) and (link.find('.png') == -1):
        return True
    return False

def formalizeLink(link):
    formalizedLink = link
    formalizedLink = formalizedLink.replace('\t','')
    formalizedLink = formalizedLink.replace('\n','')
    formalizedLink = formalizedLink.replace(' ','')
    return formalizedLink

def completeLink(link, hostUrl, domain):
    completedLink = link
    if completedLink.find('[[site]]') != -1:
        completedLink = completedLink.replace('[[site]]',domain)
        # TODO: 参数domain的传递
    elif (completedLink.find('http') == -1):
        if (completedLink[0] == '?'):
            completedLink = hostUrl + completedLink
        elif (completedLink[0] != '/'):
            completedLink = hostUrl + '/' + completedLink
        else:
            completedLink = upperUrl(hostUrl) + completedLink
    return completedLink


# 传入一个list文件，包含所有等根域名
def getPage(urlList):
    global countPage
    # 把根域名加进队列
    links.append(urlList)
    # 先得到根域名的html文件
    for hostUrl in links:
        countPage = countPage + 1
        HEADER = {
            'Host': 'www.btcc.com',
            'Cache-Control': 'max-age=0',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch, br',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        }
        urlRequest = urllib2.Request(hostUrl)
        urlResponse = urllib2.urlopen(urlRequest)
        htmlSource = urlResponse.read()
        # 把html源码写入文件中
        fileName = createFile(countPage)
        outputFile = open(fileName, 'w+')
        outputFile.write(htmlSource)
        outputFile.close()
        # 写入完成
        return urlList

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
                link = complete(link, hostUrl, domain)
                if isLink(link) and (not alreadyExist(link)):
                     links.add(link)
                pointer = tailPos + 1

# 单元测试
if __name__ == '__main__':
    if not os.path.exists('temp/'):
        os.mkdir(r'temp/')
    getPage('https://www.btcc.com/news')
