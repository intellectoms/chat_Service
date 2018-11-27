from __future__ import unicode_literals, print_function
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings

from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

from .com.intellect.snips.nlu.ProcessNLUResponse import ProcessNLUResponse

from .com.intellect.utils.SnipsProperties import SnipsProperties
from .com.intellect.snips.nlu.Engine import Engine

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

import io
import json


# Create your views here.


@api_view(["POST"])
@parser_classes((JSONParser,))
def parse_text(request):
    '''logger.error('Snips Parse API called')
	logger.info('Something went info!')
	logger.debug('Something went debug!')
	logger.info('Something went info')
	logger.warning('Something went warning!')
	logger.error('Something went error')
	logger.critical('Something went critical!')'''

    snipsProperties = SnipsProperties()
    print(snipsProperties.get_oms_details('port'), snipsProperties.get_oms_details('ip'))
    snipsProperties = SnipsProperties()
    print(snipsProperties.get_oms_details('port'), snipsProperties.get_oms_details('ip'))
    snipsProperties = SnipsProperties()
    print(snipsProperties.get_oms_details('port'), snipsProperties.get_oms_details('ip'))

    try:

        _data = json.loads(request.body)

        print('Request Message ', _data)

        if 'text' not in _data:
            return JsonResponse(ProcessNLUResponse.sendError(_data), safe=False)

        nlu_engine = Engine()
        parsing = nlu_engine.parse_text(_data['text'])
        print("Viewww", json.dumps(parsing, indent=2))
        nluprocessor = ProcessNLUResponse(parsing)

        return JsonResponse(str(nluprocessor.processdata()), safe=False)
    except ValueError as e:
        return JsonResponse(ProcessNLUResponse.sendError(), safe=False)
