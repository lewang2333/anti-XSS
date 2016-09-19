import urllib2

# from application.models.page import Page
from urlparse import urlparse

class Page(object):
    '''
    A class to store the page
    '''

    url = ''
    html = ''

    def __init__(self, url='', html=''):
        self.url = url
        self.html = html

        pass

    def get_html(self):
        return self.html


def scan(row_url):
    '''
    Main engine to scan a URL
    '''

    # formalize
    url_str = add_protocol(row_url)

    # BFS\
    urls = []
    urls.append(url_str)

    print url_str

    for temp_url in urls:
        urls.extend(find_url(temp_url))

    return result_html

def add_protocol(row_url):
    '''
    Add HPPT protocol
    '''

    if (row_url.lower().strip().find('http://') == -1) and (row_url.lower().strip().find('https://') == -1):
        return 'http://' + row_url.lower().strip()

    return row_url

def get_html(url):
    '''
    Get HTML code
    '''

    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()

    # print html
    return html

def find_url(url):
    '''
    Find all URLs in a page
    '''

    urls = []
    html = get_html(url)
    length = len(html)
    front = 0

    flag = False
    while (front <= length):
        if html.find('<a href=\"',front) == -1:
            break
        flag = True
        tail = html.find('\"',front + 12)
        link = html[html.find('<a href=',front) + 9: tail]
        urls.append(link)
        print link
        front = tail
        if not flag:
            break

    print urls
    return urls

scan('https://www.btcc.com/news')
