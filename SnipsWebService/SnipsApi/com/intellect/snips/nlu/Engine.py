from snips_nlu import SnipsNLUEngine, load_resources
from snips_nlu.default_configs import CONFIG_EN

import sys
import io
import json


class Engine:
    """ A SnipsProperties singleton class """

    class __impl:

        __nlu_engine = None

        def __init__(self):
            print('Load NLU Engine');
            print('-----------------------------------------------------------------');

            try:
                with io.open("oms_dataset.json") as f:
                    dataset = json.load(f)
            except:
                print('I/O error({0}): {1}')
                sys.exit()

            load_resources('snips_nlu_en')
            self.__nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
            self.__nlu_engine.fit(dataset)
            self.__nlu_engine.to_byte_array()


        def parse_text(self, text):
            return self.__nlu_engine.parse(text)
    # storage for the instance reference
    __instance = None

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if Engine.__instance is None:
            # Create and remember instance
            Engine.__instance = Engine.__impl()
        # Store instance reference as the only member in the handle
        self.__dict__['_SnipsProperties__instance'] = Engine.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)