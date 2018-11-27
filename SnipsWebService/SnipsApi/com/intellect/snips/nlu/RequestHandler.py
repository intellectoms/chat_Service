import requests
import json
import time
from .HttpClient import HttpClient
from .NluResponse import NluResponse
from  SnipsApi.com.intellect.utils.SessionUtils import SessionUtils

class RequestHandler():

     


    
    def accountsummary(receivedIntent,userID,sessionContext,sessionCookies ,instument):
        action = '/MarginStatement.do'
        accountSummaryReqObj = {'sendResponseFormat': 'JSON', 'sessionContext': sessionContext,'lang1': 'default' ,'marginGroupNo': '1' ,'currency': 'PHP','onbehalfid': userID ,'sendersubid': userID ,'clientid': userID }
        http_client = HttpClient
        accountsSummaryResp = http_client.sendData(action,accountSummaryReqObj,sessionCookies)
        print("Account Summary Response " ,accountsSummaryResp.text)

        accountSummaryRespJSON = json.loads(accountsSummaryResp.text)
        responseCode = accountSummaryRespJSON['responseCode']
        if(responseCode == 1002):
            nlu_response = NluResponse()
            nlu_response.response_code = 1001
            nlu_response.response_message = 'Session expired'
            return nlu_response.response_data()

        marginStatementlist = accountSummaryRespJSON['responseObject']['marginStatementlist']
        buyingPower = marginStatementlist[0]['buyingPower']
        margin = marginStatementlist[0]['margin']
        nlu_response = NluResponse()
        nlu_response.response_message = 'You have a Buying power of  {} Pesos with an available margin of ' \
                                       ' {} pesos in your margin account'.format(buyingPower,margin)
        return nlu_response.response_data()

    def cash(receivedIntent,userID,sessionContext,sessionCookies ,instument):
        action = '/CashStatement_ng.do'
        cashReqObj = {'sendResponseFormat': 'JSON','ignoreGlobalParams': 'true' ,'sessionContext': sessionContext, 'lang1': 'default' ,'marginGroupNo': '1' ,'currency': 'PHP','clientid': userID }
        http_client = HttpClient
        cashSummaryResp = http_client.sendData(action,cashReqObj,sessionCookies)
       

        cashSummaryRespJSON = json.loads(cashSummaryResp.text)
        
        responseCode = cashSummaryRespJSON['responseCode']
        if(responseCode == 1002):
            nlu_response = NluResponse()
            nlu_response.response_code = 1001
            nlu_response.response_message = 'Session expired'
            return nlu_response.response_data()

        cashStatementlist = cashSummaryRespJSON['responseObject']['cashStatementList']
        cashAvailable = cashStatementlist[0]['freeCashAvailable']
        print("cashSummaryResp" ,cashSummaryResp.text)
        
        nlu_response = NluResponse()
        nlu_response.response_message = 'Cash Available in your account is {} pesos'.format(cashAvailable)
        return nlu_response.response_data()

    def highprice(receivedIntent,userID,sessionContext,sessionCookies,instument):
        action = '/getquoteView.do'
        highpriceReqObj = {'sendResponseFormat': 'JSON', 'sessionContext': sessionContext,'symbol': instument,'exchange':'PSE','showQuote': 'YES','selectProduct': 'EQUITY','board': 'NR' ,'currency': 'PHP','clientid': userID ,'onbehalfid': userID ,'sendersubid': userID }
        http_client = HttpClient
        highpriceResp = http_client.sendData(action,highpriceReqObj,sessionCookies)
        highPriceRespJSON = json.loads(highpriceResp.text)
        responseCode = highPriceRespJSON['responseCode']
        if(responseCode == 1002):
            nlu_response = NluResponse()
            nlu_response.response_code = 1001
            nlu_response.response_message = 'Session expired'
            return nlu_response.response_data()
        nlu_response = NluResponse()
        if highPriceRespJSON['responseCode'] == 1001:
            nlu_response.response_message = 'Please try with a valid Stock'
        else:
            highPrice = highPriceRespJSON['responseObject']['quotelist'][0]['high']
            nlu_response.response_message = '{} touched an intraday high price of {} Pesos '.format(instument,highPrice)
        return nlu_response.response_data()
        
    def lowprice(receivedIntent,userID,sessionContext,sessionCookies,instument):
        action = '/getquoteView.do'
        lowpriceReqObj = {'sendResponseFormat': 'JSON', 'sessionContext': sessionContext,'symbol': instument,'exchange':'PSE','showQuote': 'YES','selectProduct': 'EQUITY','board': 'NR' ,'currency': 'PHP','clientid': userID ,'onbehalfid': userID ,'sendersubid': userID }
        http_client = HttpClient
        lowpriceResp = http_client.sendData(action,lowpriceReqObj,sessionCookies)
        lowPriceRespJSON = json.loads(lowpriceResp.text)
        responseCode = lowPriceRespJSON['responseCode']
        if(responseCode == 1002):
            nlu_response = NluResponse()
            nlu_response.response_code = 1001
            nlu_response.response_message = 'Session expired'
            return nlu_response.response_data()
        if(responseCode == 1002):
            nlu_response = NluResponse()
            nlu_response.response_code = 1001
            nlu_response.response_message = 'Session expired'
            return nlu_response.response_data()
        nlu_response = NluResponse()
        if lowPriceRespJSON['responseCode'] == 1001:
            nlu_response.response_message = 'Please try with a valid Stock'
        else:
            lowPrice = lowPriceRespJSON['responseObject']['quotelist'][0]['low']
            nlu_response.response_message = '{} touched an intraday low price of {} Pesos '.format(instument,lowPrice)
        return nlu_response.response_data()

    def askdetails(receivedIntent,userID,sessionContext,sessionCookies,instument):
        action = '/getquoteView.do'
        askReqObj = {'sendResponseFormat': 'JSON', 'sessionContext': sessionContext,'symbol': instument,'exchange':'PSE','showQuote': 'YES','selectProduct': 'EQUITY','board': 'NR' ,'currency': 'PHP','clientid': userID ,'onbehalfid': userID ,'sendersubid': userID }
        http_client = HttpClient
        askResp = http_client.sendData(action,askReqObj,sessionCookies)
        askRespJSON = json.loads(askResp.text)
        responseCode = askRespJSON['responseCode']
        if(responseCode == 1002):
            nlu_response = NluResponse()
            nlu_response.response_code = 1001
            nlu_response.response_message = 'Session expired'
            return nlu_response.response_data()
        nlu_response = NluResponse()
        if askRespJSON['responseCode'] == 1001:
            nlu_response.response_message = 'Please try with a valid Stock'
        else:
            askPrice = askRespJSON['responseObject']['quotelist'][0]['offerDepthList'][0]['offerPrice']
            askQty = askRespJSON['responseObject']['quotelist'][0]['offerDepthList'][0]['offerQty']
            nlu_response.response_message = 'Ask Details for {}: The best ask for {} is at a price' \
                                        ' of {} Pesos and ask quantity of {} '.format(instument,instument,askPrice,askQty)
        return nlu_response.response_data()

    def biddetails(receivedIntent,userID,sessionContext,sessionCookies,instument):
        action = '/getquoteView.do'
        bidReqObj = {'sendResponseFormat': 'JSON', 'sessionContext': sessionContext,'symbol': instument,'exchange':'PSE','showQuote': 'YES','selectProduct': 'EQUITY','board': 'NR' ,'currency': 'PHP','clientid': userID ,'onbehalfid': userID ,'sendersubid': userID }
        http_client = HttpClient
        bidResp = http_client.sendData(action,bidReqObj,sessionCookies)
        bidRespJSON = json.loads(bidResp.text)
        responseCode = bidRespJSON['responseCode']
        if(responseCode == 1002):
            nlu_response = NluResponse()
            nlu_response.response_code = 1001
            nlu_response.response_message = 'Session expired'
            return nlu_response.response_data()
        nlu_response = NluResponse()

        if bidRespJSON['responseCode'] == 1001:
            nlu_response.response_message = 'Please try with a valid Stock'
        else:
            bidPrice = bidRespJSON['responseObject']['quotelist'][0]['bidDepthList'][0]['bidPrice']
            bidQty = bidRespJSON['responseObject']['quotelist'][0]['bidDepthList'][0]['bidQty']
            nlu_response.response_message = 'Bid Details for {}: The best bid for {} is at a price' \
                                        ' of {} Pesos and bid quantity of {} '.format(instument,instument,bidPrice,bidQty)
        return nlu_response.response_data()

    def quote(receivedIntent,userID,sessionContext,sessionCookies,instument):
        action = '/getquoteView.do'
        quoteReqObj = {'sendResponseFormat': 'JSON', 'sessionContext': sessionContext,'symbol': instument,'exchange':'PSE','showQuote': 'YES','selectProduct': 'EQUITY','board': 'NR' ,'currency': 'PHP','clientid': userID ,'onbehalfid': userID ,'sendersubid': userID }
        http_client = HttpClient
        quoteResp = http_client.sendData(action,quoteReqObj,sessionCookies)
        quoteRespJSON = json.loads(quoteResp.text)
        responseCode = quoteRespJSON['responseCode']
        if(responseCode == 1002):
            nlu_response = NluResponse()
            nlu_response.response_code = 1001
            nlu_response.response_message = 'Session expired'
            return nlu_response.response_data()
        nlu_response = NluResponse()

        if quoteRespJSON['responseCode'] == 1001:
            nlu_response.response_message = 'Please try with a valid Stock'
        else:
            ltp = quoteRespJSON['responseObject']['quotelist'][0]['ltp']
            ltq = quoteRespJSON['responseObject']['quotelist'][0]['ltq']
            nlu_response.response_message = 'Quote Details for {}: The latest quote for {} is at a price' \
                                        ' of {} Pesos and  quantity of {} '.format(instument,instument,ltp,ltq)
        return nlu_response.response_data()


    def gainers(receivedIntent,userID,sessionContext,sessionCookies,instument):
        action = '/marketStatistics.do'
        gainerReqObj ={'sendResponseFormat': 'JSON','ignoreGlobalParams' :'true','sessionContext': sessionContext,'exchangeID':'PSE','product': 'EQUITY','requestType':'Top10Gainers' }
        http_client = HttpClient
        gainerResp = http_client.sendData(action,gainerReqObj,sessionCookies)
        gainerRespJSON = json.loads(gainerResp.text)
        responseCode = gainerRespJSON['responseCode']
        if(responseCode == 1002):
            nlu_response = NluResponse()
            nlu_response.response_code = 1001
            nlu_response.response_message = 'Session expired'
            return nlu_response.response_data()
        gainerList = gainerRespJSON['responseObject']['top10MoverList'][0]
        nlu_response = NluResponse()
        nlu_response.response_message = 'The top gaining stocks for today are '
        for item in gainerList[0:4]:
            nlu_response.response_message += ' {} up by {} .'.format(item['symbol'] ,item['changePct'])
        return nlu_response.response_data()

    def losers(receivedIntent,userID,sessionContext,sessionCookies,instument):
        action = '/marketStatistics.do'
        loserReqObj ={'sendResponseFormat': 'JSON','ignoreGlobalParams' :'true','sessionContext': sessionContext,'exchangeID':'PSE','product': 'EQUITY','requestType':'Top10Gainers' }
        http_client = HttpClient
        loserResp = http_client.sendData(action,loserReqObj,sessionCookies)
        loserRespJSON = json.loads(loserResp.text)
        responseCode = loserRespJSON['responseCode']
        if(responseCode == 1002):
            nlu_response = NluResponse()
            nlu_response.response_code = 1001
            nlu_response.response_message = 'Session expired'
            return nlu_response.response_data()
        loserList = loserRespJSON['responseObject']['top10MoverList'][1]
        nlu_response = NluResponse()
        nlu_response.response_message = 'The top losing stocks for today are '
        for item in loserList[0:4]:
            nlu_response.response_message += ' {} down by {} .'.format(item['symbol'] ,item['changePct'])
        return nlu_response.response_data()

    def hi(receivedIntent,userID,sessionContext,sessionCookies,instument):
        nlu_response = NluResponse()
        nlu_response.response_message = 'Hello, Welcome to Capital Alpha, your one stop shop for all investment needs. I can help you with stock quotes, ' \
                                        'related market information, and your account details. What would you like to know?'
        return nlu_response.response_data()
    def bye(receivedIntent,userID,sessionContext,sessionCookies,instument):
        nlu_response = NluResponse()
        nlu_response.response_message = 'Goodbye: Thanks for choosing Capital Alpha, It has been a pleasure.'
        nlu_response.response_code = 1000
        return nlu_response.response_data()

    def methodnotfound(receivedIntent,userID,sessionContext,sessionCookies,instument):
        nlu_response = NluResponse()
        nlu_response.response_code = 1001
        nlu_response.response_message = 'Sorry, that was not clear.Please try again'
        return nlu_response.response_data()

    def reLogin(self):
        sessionUtils = SessionUtils()
        sessionUtils.doLogin('login')
    
    def login(receivedIntent,userID,sessionContext,sessionCookies,instument):
        
        sessionUtils = SessionUtils()
        sessionUtils.updateSesssion()
        nlu_response = NluResponse()
        nlu_response.response_code = 0
        nlu_response.response_message = 'Logged in successfully'
        return nlu_response.response_data()

    def formRequest(self, receivedIntent ,instument):

        method = getattr(self,receivedIntent, lambda: self.methodnotfound())
        sessionUtils = SessionUtils()

        print('*************************',sessionUtils.getResponseCode('responseCode'));
        if(sessionUtils.getResponseCode('responseCode')==0):
            return method(sessionUtils.getUserId('userId'), sessionUtils.getsessionContext('sessioncontext'),
                      sessionUtils.getCookies('cookies'), instument)
        else :
            sessionUtils.updateSesssion()
            if(sessionUtils.getResponseCode('responseCode')==0):
                return method(sessionUtils.getUserId('userId'), sessionUtils.getsessionContext('sessioncontext'),
                              sessionUtils.getCookies('cookies'), instument)
            else:
                return self.methodnotfound()