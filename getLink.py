#encoding: utf8

def getLink(src):
    source = src.lower()
    links = []
    head = 0
    length = len(source)
    flag = True
    while ((flag) and (head < length)):
        flag = False
        pos1 = source[head:].find('href="') + head
        pos2 = source[head + pos1:].find('</script>') + head + pos1
        if (pos1 >= head)and(pos2 >= head):
            flag = True
            link = source[pos1:pos2 + 9]
            link = link.replace('\t','')
            link = link.replace('\n','')
            link = link.replace(' ','')
            links.append(link)
            head = pos2 + 10

    for i in links:
        print i

    return links
