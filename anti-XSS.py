#coding: utf8

from getLink import getLink

def main():
    domain = 'https://www.btcc.com'
    f = open('page.txt','rb')
    src = f.read()
    getLink(src, domain)
    f.close()

if __name__ == '__main__':
    main()
