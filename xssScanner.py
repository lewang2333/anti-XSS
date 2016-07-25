#coding: utf8

def xssScanner(filename):
    f1 = open(filename,'rb')
    f2 = open('xss','w+')

    # This payload has alreadly transform to lowercase bucause the file is lowercase.
    payload = f1.readline()
    while (payload != ''):

        # case 0: safe; 1: notsafe; 2: vulnerable
        if (payload.find('cookie') > -1):
            case = 2
        elif (payload.find('document') > -1):
            case = 2
        elif (payload.find('open') > -1):
            case = 1
        elif (payload.find('alert') > -1):
            case = 1
        else:
            case = 0

        f2.write(payload + '\t' + str(case) + '\n')

        payload = f1.readline()


    f1.close()
    f2.close()
