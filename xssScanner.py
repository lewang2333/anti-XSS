#coding: utf8

def xssScanner(filename):

    result = []

    f1 = open(filename,'rb')
    f2 = open('xss.txt','w+')

    # This payload has alreadly transform to lowercase bucause the file is lowercase.
    payload = f1.readline()
    while (payload != ''):

        # case 0: safe; 1: notsafe; 2: vulnerable
        if (payload.find('cookie') > -1):
            case = 2
        # elif ((payload.find('document') > -1) and (payload.find('olark') == -1) and (payload.find('baidu') == -1) and (payload.find('google') == -1)):
        #     case = 2
        # elif ((payload.find('open') > -1) and (payload.find('olark') == -1) and (payload.find('baidu') == -1) and (payload.find('google') == -1)):
        #     case = 1
        # elif ((payload.find('alert') > -1) and (payload.find('olark') == -1) and (payload.find('baidu') == -1) and (payload.find('google') == -1)):
        #     case = 1
        else:
            case = 0

        result.append((payload, case))
        # f2.write(payload + '\t' + str(case) + '\n')

        payload = f1.readline()

    # for i in result:
    #     f2.write(i)

    f2.write('# XSS Scan Result\n')
    f2.write('## High Vulnerable Level Script\n')
    for i in result:
        if i[1] == 2:
            f2.write(i[0] + '\n')
    f2.write('## Mid Vulnerable Level Script\n')
    for i in result:
        if i[1] == 1:
            f2.write(i[0] + '\n')

    f1.close()
    f2.close()
