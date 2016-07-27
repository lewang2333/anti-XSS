#coding: utf8

from lib.parse.cmdline import cmdLineParser

def main():
    try:
        cmdLineParser()
    except Exception as e:
        print e

if __name__ == '__main__':
    main()
