# Return the html source of the src website
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

    return page
