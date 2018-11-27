import configparser
import sys


class SnipsProperties:

    """ A SnipsProperties singleton class """

    class __impl:

        __config = None
        __oms_prop = None
        """ Implementation of the singleton interface
         http://code.activestate.com/recipes/52558-the-singleton-pattern-implemented-with-python/
         """

        def __init__(self):
            self.__config = configparser.ConfigParser()
            self.__config.sections()
            try:
                print("Loading Properties Value")
                self.__config.read('SnipsProperties.ini')
                self.__oms_prop = self.__config['oms-details']
            except:
                print('I/O error({0}): {1}')
                sys.exit()

            print("Snips Properties file Loaded ")

        def get_oms_details(self, prop_name):
            return self.__oms_prop[prop_name]

    # storage for the instance reference
    __instance = None

    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if SnipsProperties.__instance is None:
            # Create and remember instance
            SnipsProperties.__instance = SnipsProperties.__impl()
        # Store instance reference as the only member in the handle
        self.__dict__['_SnipsProperties__instance'] = SnipsProperties.__instance

    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)






