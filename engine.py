#coding: utf8
import urllib
import urllib2

# 网页个数
countPage = 0
# 所有扫描到的链接
links = []
# TODO: 把domain定义成全局变量
domain = 'https://www.btcc.com/news'

def createFile(countPage):
    fileName = '/tmp/' + str(countPage)
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
    # 把根域名加进队列
    links.append(urlList)
    # 先得到根域名的html文件
    for hostUrl in links:
        countPage = countPage + 1
        urlRequest = urllib2.request(hostUrl)
        urlResponse = urllib2.urlopen(urlRequest)
        htmlSource = urlRequest.read()
        # 把html源码写入文件中
        fileName = createFile(countpage)
        outputFile = open(fileName, 'w+')
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
                link = complete(link, hostUrl, domain)
                if isLink(link) and (!alreadyExist(link)):
                     links.add(link)
                pointer = tailPos + 1

# 单元测试
if __name__ == '__main__':
    getPage('https://www.btcc.com/news')
