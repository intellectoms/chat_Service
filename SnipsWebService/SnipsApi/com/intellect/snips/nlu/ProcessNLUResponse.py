import json


from .NluResponse import NluResponse
from .Switcher import Switcher

class ProcessNLUResponse:

    '''Process NLU response'''

    def __init__(self,nluresponsedata):
        self.nluresponsedata = nluresponsedata

    def processdata(self):
        switcher = Switcher()
        response_data = switcher.parse_nlu_response(self.nluresponsedata)
        return response_data

    def sendError(self):
        nlu_response = NluResponse()
        nlu_response.response_code = 1001
        nlu_response.response_message = 'Something went wrong'
        return nlu_response.response_data()










