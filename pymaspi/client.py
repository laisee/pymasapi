'''
Module for retrieving data from MAS site
'''
import settings
import string

from helpers import get_response

class Client(object):
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
        return get_response(cls.URL, resourceid, params)

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
        return get_response(cls.URL, resourceid, params)

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
        return get_response(cls.URL, resourceid, params)

    def money_supply_dbu(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = None
        if string.lower(period) == "m":
            resourceid = settings.MONEY_SUPPLY_DBU_MONTHLY 
        elif string.lower(period) == "y":
            resourceid = settings.MONEY_SUPPLY_DBU_ANNUAL 
        else:
            raise ValueError("Invalid value for time period %s " % period)
        return get_response(cls.URL, resourceid, params)

    def credit_card(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = None
        if string.lower(period) == "m":
            resourceid = settings.CREDIT_CARD_MONTHLY 
        elif string.lower(period) == "y":
            resourceid = settings.CREDIT_CARD_ANNUAL 
        else:
            raise ValueError("Invalid value for time period %s " % period)
        return get_response(cls.URL, resourceid, params)

    def mas_asset_liability(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = None
        if string.lower(period) == "m":
            resourceid = settings.MAS_ASSET_LIABILITY_MONTHLY 
        elif string.lower(period) == "y":
            resourceid = settings.MAS_ASSET_LIABILITY_MONTHLY 
        else:
            raise ValueError("Invalid value for time period %s " % period)
        return get_response(cls.URL, resourceid, params)

    def asian_dollar_assets(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = None
        if string.lower(period) == "m":
            resourceid = settings.ASIAN_DOLLAR_ASSETS_MONTHLY 
        elif string.lower(period) == "y":
            resourceid = settings.ASIAN_DOLLAR_ASSETS_ANNUAL
        else:
            raise ValueError("Invalid value for time period %s " % period)
        return get_response(cls.URL, resourceid, params)

    def deposits_dbu_nonbank(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = None
        if string.lower(period) == "m":
            resourceid = settings.DEPOSITS_DBU_NONBANK_MONTHLY 
        elif string.lower(period) == "y":
            resourceid = settings.DEPOSITS_DBU_NONBANK_ANNUAL
        else:
            raise ValueError("Invalid value for time period %s " % period)
        return get_response(cls.URL, resourceid, params)

    def loan_dbu_nonbank_byindustry(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = None
        if string.lower(period) == "m":
            resourceid = settings.LOAN_DBU_NONBANK_BYINDUSTRY_MONTHLY 
        elif string.lower(period) == "y":
            resourceid = settings.LOAN_DBU_NONBANK_BYINDUSTRY_ANNUAL
        else:
            raise ValueError("Invalid value for time period %s " % period)
        return get_response(cls.URL, resourceid, params)

    def loan_acu_nonbank_byindustry(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = None
        if string.lower(period) == "m":
            resourceid = settings.LOAN_ACU_NONBANK_BYINDUSTRY_MONTHLY 
        elif string.lower(period) == "y":
            resourceid = settings.LOAN_ACU_NONBANK_BYINDUSTRY_ANNUAL
        else:
            raise ValueError("Invalid value for time period %s " % period)
        return get_response(cls.URL, resourceid, params)

    def loan_finance(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = None
        if string.lower(period) == "m":
            resourceid = settings.FINANCE_LOAN_MONTHLY 
        elif string.lower(period) == "y":
            resourceid = settings.FINANCE_LOAN_ANNUAL
        else:
            raise ValueError("Invalid value for time period %s " % period)
        return get_response(cls.URL, resourceid, params)

    def sgxst(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = None
        if string.lower(period) == "m":
            resourceid = settings.SGXST_MONTHLY 
        elif string.lower(period) == "y":
            resourceid = settings.SGXST_ANNUAL
        else:
            raise ValueError("Invalid value for time period %s " % period)
        return get_response(cls.URL, resourceid, params)

if __name__ == '__main__':
    c = Client()
    data = c.sgxst("y",100)
    if data:
        for record in data["result"]["records"]:
            print record
