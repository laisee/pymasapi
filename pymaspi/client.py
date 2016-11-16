'''
Module for retrieving data from MAS site
'''
import settings
from helpers import get_response

class Client:
    ''' Class for retrieving data from MAS site '''


    def __init__(cls):
        cls.URL = "{0:s}://{1:s}".format(settings.PROTOCOL, settings.BASE_URL)
        pass

    def interest_rates(cls, limit=5):
        resourceid = 'b5adb5c2-4604-49f3-b924-b69691252380'
        params = "&limit=%s" % limit
        data = get_response(cls.URL, resourceid, params)
        for record in data["result"]["records"]:
            print record["interbank_1m"]

if __name__ == '__main__':
    c = Client()
    data = c.interest_rates(10)
    print data
