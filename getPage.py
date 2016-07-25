# Return the html source of the src website

import urllib
import urllib2

def getPage(src):

    hosturl = src

    header = {
    }

    postdata = ''

    enpostdata = urllib.urlencode(postdata)
    urlrequest = urllib2.Request(hosturl)
    urlresponse = urllib2.urlopen(urlrequest)

    page = urlresponse.read()
    # print page

    f = open('page.txt','w')
    f.write(page)
    f.close()

    return page

if __name__ == '__main__':
    getPage('https://www.btcc.com')
