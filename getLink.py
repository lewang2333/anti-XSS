#encoding: utf8

# Return a set of url links in src page
def getLink(src):
    source = src.lower()
    links = set()
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
            links.add(link)
            head = pos2 + 1

    # print links[0]
    # print links[1]
    # for i in links:
    #     print i

    return links

if __name__ == '__main__':
    f = open('page.txt','rb')
    src = f.read()
    getLink(src)
    f.close()
