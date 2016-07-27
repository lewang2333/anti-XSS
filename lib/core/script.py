
class Script(object):
    __payload = ''
    __fromDomain = ''
    __danger = False

    def __init__(self, payload='', fromDomain='', danger=False):
        self.__payload = payload
        self.__fromDomain = fromDomain
        self.__danger = danger

    def setPayload(payload):
        self.__payload = payload

    def setFromDomain(fromDomain):
        self.__fromDomain = fromDomain

    def setDanger(danger):
        self.__danger = danger

    def getPayload(self):
        return self.__payload

    def getFromDomain(self):
        return self.__fromDomain

    def getDanger(self):
        return self.__danger

    def find(self, target):
        return self.__payload.find(target)
