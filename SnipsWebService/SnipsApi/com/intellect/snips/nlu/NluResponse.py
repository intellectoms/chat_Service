import json


class NluResponse(object):

    def __init__(self):
        self._response_code = 0
        self._response_message = ''
        self._context_business_map = ''
        self._probability_intent_list = ''

    def get_response_object(self):
        return json.dumps(vars(self), sort_keys=True, indent=4)

    @property
    def response_code(self):
        return self._response_code

    @response_code.setter
    def response_code(self, response_code):
        self._response_code = response_code

    @property
    def response_message(self):
        return self._response_message

    @response_message.setter
    def response_message(self, response_message):
        self._response_message = response_message

    @property
    def context_business_map(self):
        return self._context_business_map

    @context_business_map.setter
    def context_business_map(self, context_business_map):
        self._context_business_map = context_business_map

    @property
    def probability_intent_list(self):
        return self.probability_intent_list

    @probability_intent_list.setter
    def context_business_map(self, probability_intent_list):
        self._probability_intent_list = probability_intent_list

    def quote(self):
        nlu_response = NluResponse()
        nlu_response.response_message = 'The current Ask or Offer quantity for YESBANK is 573'
        return nlu_response

    def __str__(self):
        return 'NluResponse(_response_code=' + self._response_code + ', message =' + str(self.response_message) + ')'

    def response_data(self):
        print("json Dump ", json.dumps(self.__dict__, indent=2));
        return json.dumps(self.__dict__)

