#encoding: utf8

from getPage import *
from upperUrl import *

# links ia a global set that stroe all of the links in the particular domain.
links = set()
domain = 'https://www.btcc.com'

# Return a set of url links in src page
def getLink(filename, url):
    f = open(filename,'rb')
    source = f.read().lower()
    f.close()
    # links = set()
    head = 0
    length = len(source)
    flag = True
    while ((flag) and (head < length)):
        flag = False
        pos1 = source[head:].find('href="') + head
        pos2 = source[pos1 + 7:].find('"') + pos1 + 7


        if (pos1 >= head)and(pos2 >= head):

            # print pos1, pos2 ,head

            flag = True
            link = source[pos1 + 6:pos2]
            link = link.replace('\t','')
            link = link.replace('\n','')
            link = link.replace(' ','')

            # Fill up link
            if link.find('[[site]]') != -1:
                link = link.replace('[[site]]',domain)
            elif (link.find('http') == -1):
                if (link[0] == '?'):
                    link = url + link
                elif (link[0] != '/'):
                    link = url + '/' + link
                else:
                    link = upperUrl(url) + link

            if (link.find('btcc') > -1) and (link.find('.png') == -1):
                 links.add(link)
                #  getPage(link)

            head = pos2 + 1

    f = open(filename.replace('.pg','.lk'),'w+')
    for i in links:
        f.write(i + '\n')
    f.close()

    return filename.replace('.pg','.lk')
