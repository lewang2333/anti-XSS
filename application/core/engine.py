from models.page import Page

from urlparse import urlparse

def scan(row_url):
    '''
    Main engine to scan a URL
    '''

    # formalize
    url_str = add_protocol(row_url)

    # BFS
    urls = []
    urls.append(url_str)

    for new_url in urls:
        html = get_html(new_url)
        page = Page(url=new_url, html=html)
        urls.extend(page)

    return result_html

def add_protocol(row_url):
    '''
    Add HPPT protocol
    '''

    if (row_url.lower().strip().find('http://') == -1) and (row_url.lower().strip().find('https://') == -1):
        return 'http://' + row_url.lower().strip()

    pass

def get_html(url):
    '''
    Get HTML code
    '''

    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()

    return html

def find_url(page):
    '''
    Find all URLs in a page
    '''

    urls = []
    html = page.get_html()
    url = page.get_url()
    length = len(html)
    front = 0

    while (front <= length):
        if html.find('<a href=',front) == -1:
            continue
        tail = html.find('a>',front)
        link = html[html.find('<a href=',front) + 9: tail]
        urls.append(link)

    return urls
