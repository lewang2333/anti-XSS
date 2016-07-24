def findScript(page):
    source = page.lower()
    payloads = []
    head = 0
    length = len(source)
    flag = True
    while ((flag) and (head < length)):
        flag = False
        pos1 = source[head:].find('<script') + head
        pos2 = source[head:].find('</script>') + head
        if (pos1 >= head)and(pos2 >= head):
            flag = True
            payload = source[pos1:pos2 + 9]
            payload = payload.replace('\t','')
            payload = payload.replace('\n','')
            payload = payload.replace(' ','')
            payloads.append(payload)
            head = pos2 + 10

    return payloads
