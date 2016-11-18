'''
Module for retrieving data from MAS site
'''
import settings
import string

from helpers import get_response

class Client:
    ''' Class for retrieving data from MAS site '''


    def __init__(cls):
        cls.URL = "{0:s}://{1:s}".format(settings.PROTOCOL, settings.BASE_URL)
        pass

    def exchange_rates_end(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = None
        if string.lower(period) == "d":
            resourceid = settings.EXCHANGE_RATES_END_DAILY 
        elif string.lower(period) == "w":
            resourceid = settings.EXCHANGE_RATES_END_WEEKLY 
        elif string.lower(period) == "m":
            resourceid = settings.EXCHANGE_RATES_END_MONTHLY 
        elif string.lower(period) == "y":
            resourceid = settings.EXCHANGE_RATES_END_ANNUAL 
        else:
            raise ValueError("Invalid value for time period %s " % period)
        data = get_response(cls.URL, resourceid, params)

    def exchange_rates_average(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = None
        if string.lower(period) == "w":
            resourceid = settings.EXCHANGE_RATES_AVERAGE_WEEKLY 
        elif string.lower(period) == "m":
            resourceid = settings.EXCHANGE_RATES_AVERAGE_MONTHLY 
        elif string.lower(period) == "y":
            resourceid = settings.EXCHANGE_RATES_AVERAGE_ANNUAL 
        else:
            raise ValueError("Invalid value for time period %s " % period)

        data = get_response(cls.URL, resourceid, params)

    def interest_rates(cls, type, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = None
        if type is None:
            raise ValueError("Type cannot be empty")
        if period is None:
            raise ValueError("Period cannot be empty")
        if string.lower(period) == "w":
            resourceid = settings.INTEREST_RATES_DOMESTIC_WEEKLY if type == "dom" else None
        elif string.lower(period) == "m":
            resourceid = settings.INTEREST_RATES_DOMESTIC_MONTHLY if type == "dom" else settings.INTEREST_RATES_FINANCE_MONTHLY
        elif string.lower(period) == "y":
            resourceid = settings.INTEREST_RATES_DOMESTIC_ANNUAL if type == "dom" else settings.INTEREST_RATES_FINANCE_ANNUAL
        else:
            raise ValueError("Invalid value for time period %s " % period)

        if resourceid is None:
            raise ValueError("Invalid period %s for Weekly interest rates of type %s" % (period, type))

        data = get_response(cls.URL, resourceid, params)

    def money_supply_dbu(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = None
        if string.lower(period) == "m":
            resourceid = settings.MONEY_SUPPLY_DBU_MONTHLY 
        elif string.lower(period) == "y":
            resourceid = settings.MONEY_SUPPLY_DBU_ANNUAL 
        else:
            raise ValueError("Invalid value for time period %s " % period)

        data = get_response(cls.URL, resourceid, params)

    def credit_card(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = None
        if string.lower(period) == "m":
            resourceid = settings.CREDIT_CARD_MONTHLY 
        elif string.lower(period) == "y":
            resourceid = settings.CREDIT_CARD_ANNUAL 
        else:
            raise ValueError("Invalid value for time period %s " % period)

        data = get_response(cls.URL, resourceid, params)

if __name__ == '__main__':
    c = Client()
    data = c.money_supply_dbu("y",1)
    if data:
        for record in data["result"]["records"]:
            print record["interbank_1m"]
