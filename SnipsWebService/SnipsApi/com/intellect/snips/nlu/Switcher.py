
from .NluResponse import NluResponse
from .RequestHandler import RequestHandler
import requests
import json
import time


class Switcher(object):
    def parse_nlu_response(self, nlu_response):
        instument = ""
        isLoggedin = False
        """Dispatch method"""
        self.nlu_response = nlu_response
        if nlu_response['intent'] is None or nlu_response['intent']['probability'] < 0.5:
            return self.methodnotfound()

        if nlu_response['slots'] is not None  and len(nlu_response['slots']) > 0 and nlu_response['slots'][0] is not None \
                and nlu_response['slots'][0]['rawValue'] is not None:
            
            self._instrument = nlu_response['slots'][0]['value']['value']
            instument = nlu_response['slots'][0]['value']['value']
            print('instument ' ,instument)
        receivedIntent = str(nlu_response['intent']['intentName'])
        nlu_response = NluResponse()
        nlu_response.response_code = 1001
        nlu_response.response_message = 'Sorry, that was not clear.Please try again'

        if isLoggedin == True:
              method_name = str(nlu_response['intent']['intentName'])
              method = getattr(self, method_name, lambda: nlu_response.response_data())
              return method()
        else:
             print("--------------else")
             request_Handler = RequestHandler()
             return request_Handler.formRequest(receivedIntent,instument)
        # Call the method as we return it
       


        

    def methodnotfound(self):
        nlu_response = NluResponse()
        nlu_response.response_code = 1001
        nlu_response.response_message = 'Sorry, that was not clear.Please try again'
        return nlu_response.response_data()

    def accountsummary(self):
        nlu_response = NluResponse()
        nlu_response.response_message = 'You have a Buying power of INR 40890.65 with an available margin of ' \
                                       'INR 25625.80 in your margin account'
        return nlu_response.response_data()

    def askdetails(self):
        nlu_response = NluResponse()
        nlu_response.response_message = 'Ask or Offer details for '+self._instrument+' . The best ask for '+ self._instrument +' is at a' \
                                        ' price of 226.05 Indian Rupees and ask quantity of 573'
        return nlu_response.response_data()

    def biddetails(self):
        nlu_response = NluResponse()
        nlu_response.response_message = 'Bid Details for '+self._instrument+': The best bid for '+ self._instrument +' is at a price' \
                                        ' of 13.91 Indian Rupees and bid quantity of 200 '
        return nlu_response.response_data()

    def buyingpower(self):
        nlu_response = NluResponse()
        nlu_response.response_message = 'You have a Buying power of INR 40890.65  in your margin account for trading '
        return nlu_response.response_data()

    def gainers(self):
        nlu_response = NluResponse()
        nlu_response.response_message = 'The top gaining stocks for today are: 1, HPCL, up 4.44% 2, Yes Bank, up 4.42% 3 ' \
                                        ',Asian Paints, up 3.82% 4, Sun Pharma, up 3.07% 5, BPCL, up 2.53%'
        return nlu_response.response_data()

    def highprice(self):
        nlu_response = NluResponse()
        nlu_response.response_message = self._instrument+' touched an intraday high price of 287.50 Indian Rupees '
        return nlu_response.response_data()

    def losers(self):
        nlu_response = NluResponse()
        nlu_response.response_message = 'The top losing stocks for today are: (Number 1)Infosys,' \
                                        ' down 2.44% (Number 2)Bharti Airtel, down 2.19% (Number 3)Hindalco, down 2.14% ' \
                                        '(Number 4)Wipro, down 1.85% (Number 5)Doctor Reddy s Labs, down 1.80%'

        return nlu_response.response_data()

    def lowprice(self):
        nlu_response = NluResponse()
        nlu_response.response_message = self._instrument+ ' touched an intraday low price of 287.50 Indian Rupees '
        return nlu_response.response_data()

    def quote(self):
        nlu_response = NluResponse()
        nlu_response.response_message =  self._instrument+ ' is trading at 528.50 INR, down 0.96% from yesterday. '
        return nlu_response.response_data()

    def hi(self):
        nlu_response = NluResponse()
        nlu_response.response_message = 'Hello, Welcome to Capital Alpha, your one stop shop for all investment needs. I can help you with stock quotes, ' \
                                        'related market information, and your account details. What would you like to know?'
        return nlu_response.response_data()

    def bye(self):
        nlu_response = NluResponse()
        nlu_response.response_message = 'Goodbye: Thanks for choosing Capital Alpha, It has been a pleasure.'
        nlu_response.response_code = 1000
        return nlu_response.response_data()


