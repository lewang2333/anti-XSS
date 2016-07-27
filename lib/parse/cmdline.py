from optparse import OptionParser

def cmdLineParser():
    '''
    cmdLineParser
    '''
    parser = OptionParser()
    parser.add_option('-v', '--version', dest='showVersion', action='store_true', help='Show program\'s version number and exit')
    parser.add_option('-u', '--url', dest='url', help='Target URL (e.g. \'http://www.site.com/\')')
    (options, args) = parser.parse_args()
