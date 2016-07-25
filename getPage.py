# Return the html source of the src website

import urllib
import urllib2

def getPage(src):

    hosturl = src

    HEADER = {
        'GET': '/ HTTP/1.1',
        'Host': 'www.btcc.com',
        'Connection': 'close',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cookie': ''
    }

    postdata = ''

    urlrequest = urllib2.Request(hosturl)

    enpostdata = urllib.urlencode(postdata)
    urlrequest = urllib2.Request(hosturl)
    # urlrequest.add_header(HEADER)
    urlresponse = urllib2.urlopen(urlrequest)

    page = urlresponse.read()
    # print page

    f = open('page.txt','w+')
    f.write(page)
    f.close()

    return page

if __name__ == '__main__':
    getPage('https://www.btcc.com/news/')
