
class Link(object):

    __url = ''
    __domain = ''
    __page = ''

    def __init__(self, url='', domain='', page=''):
        self.__url = url
        self.__domain = domain
        self.__page = page

    def getUrl(self):
        return self.__url

    def getDomain(self):
        return self.__domain

    def getPage(self):
        return self.__page

    def setUrl(self, url):
        self.__url = url

    def setDomain(self, domain):
        self.__domain = domain

    def setPage(self, page):
        self.__page = page
        
