import configparser
import sys
import json

from SnipsApi.com.intellect.snips.nlu.HttpClient import HttpClient



class SessionUtils:

    """ A SessionUtils singleton class """

    class __impl:

        __sessionCookies = None
        __sessionContext = None
        __userId = None
        __responseCode = None
        __isLoggedIn = False


        """ Implementation of the singleton interface
         """
        def doLogin(self,test):
            print("Login method Called")
            action = '/Login.do'
            reqObj = {'sendResponseFormat': 'JSON', 'loginid': 'demoinv1', 'password': 'asdad', 'lang1': 'default'}
            http_client = HttpClient
            loginresp = http_client.sendData(action, reqObj, self.__sessionCookies)
            loginResponse = json.loads(loginresp.text)
            self.__responseCode = loginResponse['responseCode']
            print("Response Code :", self.__responseCode)
            print("Login method Response", loginResponse)


            if(self.__responseCode==0):
                self.__sessionCookies = loginresp.cookies
                self.__sessionContext = loginResponse["responseObject"]["sessioncontext"]
                self.__userId = loginResponse["responseObject"]["onbehalfid"]
                self.__responseCode = 0
                self.__isLoggedIn = True
            else:
                self.__responseCode = 1000
                self.__isLoggedIn = False

        def __init__(self):

            try:
                print("Login Utils Init")
                self.doLogin('test')
            except:
                print('Some thing Went wrong in Login Utils')
                sys.exit()

        def serialize(self,object):
            return json.dumps(object, default=lambda o: o.__dict__.values()[0])

        def getSessionDetails(self,test):
            sessionDetails = {
                "sessionContext": self.__sessionContext,
                "userId": self.__userId,
                "responseCode": self.__responseCode,
                "isLoggedIn": self.__isLoggedIn
            }
            return self.serialize(sessionDetails)

        def getCookies(self,test):
            return self.__sessionCookies

        def getsessionContext(self, test):
            return self.__sessionContext

        def getUserId(self, test):
            return self.__userId

        def getResponseCode(self, test):
            return self.__responseCode


    # storage for the instance reference
    __instance = None

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if SessionUtils.__instance is None:
            # Create and remember instance
            SessionUtils.__instance = SessionUtils.__impl()
        # Store instance reference as the only member in the handle
        self.__dict__['_SessionUtils__instance'] = SessionUtils.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)

    def updateSesssion(self):
        """ Delegate access to implementation """
        SessionUtils.__instance = SessionUtils.__impl()
        self.__dict__['_SessionUtils__instance'] = SessionUtils.__instance
            






