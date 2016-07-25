#encoding: utf8

# links ia a global set that stroe all of the links in the particular domain.
links = set()

# Return a set of url links in src page
def getLink(filename, domain):
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
            if (link.find('http') == -1):
                if (link[0] != '/'):
                    link = domain + '/' + link
                else:
                    link = domain + link

            links.add(link)
            head = pos2 + 1

    # print links[0]
    # print links[1]
    f = open(filename.replace('.pg','.lk'),'w+')
    for i in links:
        f.write(i + '\n')
    f.close()

    return filename.replace('.pg','.lk')

# if __name__ == '__main__':
#     DOMAIN = 'https://www.btcc.com'
#     f = open('page.txt','rb')
#     src = f.read()
#     getLink(src)
#     f.close()
