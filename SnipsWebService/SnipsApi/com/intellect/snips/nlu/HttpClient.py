import requests
import json
import time
from .NluResponse import NluResponse

class HttpClient:
    def sendData(action,reqObj,sessionCookies):
        #url = 'http://10.10.4.43:50443'
        url = 'http://gotxdemoa.intellectdesign.com:50443/'
        
        postRequest = requests.post(url+action, cookies=sessionCookies, data=reqObj)
        return postRequest


        