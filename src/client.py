'''
Module for retrieving data from MAS site
'''

try: 
    from src.helper import get_response
except (ImportError, ModuleNotFoundError) as err:
    print(err)
    try: 
        from pymasapi.src.helper import get_response
    except (ImportError, ModuleNotFoundError) as err:
        print(err)

try: 
    from src.settings import Settings
except (ImportError, ModuleNotFoundError) as err:
    print(err)
    try: 
        from pymasapi.src.settings import Settings
    except (ImportError, ModuleNotFoundError) as err:
        print(err)


class Client(object):
    ''' Class for retrieving data from MAS site '''
    def __init__(cls):
        cls.URL = "{0:s}://{1:s}".format(Settings.PROTOCOL, Settings.BASE_URL)
        pass

    def exchange_rates_end(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = cls.get_resource_id("FXRATESEND", period)
        return get_response(cls.URL, resourceid, params)

    def exchange_rates_average(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = cls.get_resource_id("FXRATESAVG", period)
        return get_response(cls.URL, resourceid, params)

    def interest_rates(cls, period, limit=5, type=None):
        params = "&limit=%s" % limit
        resourceid = cls.get_resource_id("RATES", period, type)
        return get_response(cls.URL, resourceid, params)

    def money_supply_dbu(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = cls.get_resource_id("MONEY", period, type)
        return get_response(cls.URL, resourceid, params)

    def credit_card(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = cls.get_resource_id("CCARD", period, type)
        return get_response(cls.URL, resourceid, params)

    def mas_asset_liability(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = cls.get_resource_id("MASALM", period, type)
        return get_response(cls.URL, resourceid, params)

    def asian_dollar_assets(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = cls.get_resource_id("ADLRASSETS", period, type)
        return get_response(cls.URL, resourceid, params)

    def deposits_dbu_nonbank(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = cls.get_resource_id("DBUNONBANK", period)
        return get_response(cls.URL, resourceid, params)

    def loan_dbu_nonbank_byindustry(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = cls.get_resource_id("DBUNONBANKBYIND", period)
        return get_response(cls.URL, resourceid, params)

    def loan_acu_nonbank_byindustry(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = cls.get_resource_id("ACUNONBANKBYIND", period)
        return get_response(cls.URL, resourceid, params)

    def loan_finance(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = cls.get_resource_id("FINLOAN", period)
        return get_response(cls.URL, resourceid, params)

    def sgxst(cls, period, limit=5):
        params = "&limit=%s" % limit
        resourceid = cls.get_resource_id("SGXST", period)
        return get_response(cls.URL, resourceid, params)

    @staticmethod
    def get_resource_id(api, period, type=None):

        resourceid = None

        if api == "SGXST":
            if period.lower() == "m":
                resourceid = Settings.SGXST_MONTHLY
            elif period.lower() == "y":
                resourceid = Settings.SGXST_ANNUAL
            else:
                raise ValueError("Invalid value for time period %s " % period)
        elif api == "FINLOAN":
            if period.lower() == "m":
                resourceid = Settings.FINANCE_LOAN_MONTHLY
            elif period.lower() == "y":
                resourceid = Settings.FINANCE_LOAN_ANNUAL
            else:
                raise ValueError("Invalid value for time period %s " % period)
        elif api == "ACUNONBANKBYIND":
            if period.lower() == "m":
                resourceid = Settings.LOAN_ACU_NONBANK_BYINDUSTRY_MONTHLY
            elif period.lower() == "y":
                resourceid = Settings.LOAN_ACU_NONBANK_BYINDUSTRY_ANNUAL
            else:
                raise ValueError("Invalid value for time period %s " % period)

        elif api == "DBUNONBANKBYIND":
            if period.lower() == "m":
                resourceid = Settings.LOAN_DBU_NONBANK_BYINDUSTRY_MONTHLY
            elif period.lower() == "y":
                resourceid = Settings.LOAN_DBU_NONBANK_BYINDUSTRY_ANNUAL
            else:
                raise ValueError("Invalid value for time period %s " % period)
        elif api == "DBUNONBANK":
            if period.lower() == "m":
                resourceid = Settings.DEPOSITS_DBU_NONBANK_MONTHLY
            elif period.lower() == "y":
                resourceid = Settings.DEPOSITS_DBU_NONBANK_ANNUAL
            else:
                raise ValueError("Invalid value for time period %s " % period)
        elif api == "FXRATESEND":
            if period.lower() == "d":
                resourceid = Settings.EXCHANGE_RATES_END_DAILY
            elif period.lower() == "w":
                resourceid = Settings.EXCHANGE_RATES_END_WEEKLY
            elif period.lower() == "m":
                resourceid = Settings.EXCHANGE_RATES_END_MONTHLY
            elif period.lower() == "y":
                resourceid = Settings.EXCHANGE_RATES_END_ANNUAL
            else:
                raise ValueError("Invalid value for time period %s " % period)
        elif api == "FXRATESAVG":
            if period.lower() == "w":
                resourceid = Settings.EXCHANGE_RATES_AVERAGE_WEEKLY
            elif period.lower() == "m":
                resourceid = Settings.EXCHANGE_RATES_AVERAGE_MONTHLY
            elif period.lower() == "y":
                resourceid = Settings.EXCHANGE_RATES_AVERAGE_ANNUAL
            else:
                raise ValueError("Invalid value for time period %s " % period)
        elif api == "RATES":
            if type is None:
                raise ValueError("Type cannot be empty")
            if period is None:
                raise ValueError("Period cannot be empty")
            if period.lower() == "w":
                resourceid = Settings.INTEREST_RATES_DOMESTIC_WEEKLY if type == "dom" else None
            elif period.lower() == "m":
                resourceid = Settings.INTEREST_RATES_DOMESTIC_MONTHLY if type == "dom" else Settings.INTEREST_RATES_FINANCE_MONTHLY
            elif period.lower() == "y":
                resourceid = Settings.INTEREST_RATES_DOMESTIC_ANNUAL if type == "dom" else Settings.INTEREST_RATES_FINANCE_ANNUAL
            else:
                raise ValueError("Invalid value for time period %s " % period)
        elif api == "MONEY":
            if period.lower() == "m":
                resourceid = Settings.MONEY_SUPPLY_DBU_MONTHLY
            elif period.lower() == "y":
                resourceid = Settings.MONEY_SUPPLY_DBU_ANNUAL
            else:
                raise ValueError("Invalid value for time period %s " % period)
        elif api == "CCARD":
            if period.lower() == "m":
                resourceid = Settings.CREDIT_CARD_MONTHLY
            elif period.lower() == "y":
                resourceid = Settings.CREDIT_CARD_ANNUAL
            else:
                raise ValueError("Invalid value for time period %s " % period)
        elif api == "MASALM":
            if period.lower() == "m":
                resourceid = Settings.MAS_ASSET_LIABILITY_MONTHLY
            elif period.lower() == "y":
                resourceid = Settings.MAS_ASSET_LIABILITY_MONTHLY
            else:
                raise ValueError("Invalid value for time %s " % period)
        elif api == "ADLRASSETS":
            if period.lower() == "m":
                resourceid = Settings.ASIAN_DOLLAR_ASSETS_MONTHLY
            elif period.lower() == "y":
                resourceid = Settings.ASIAN_DOLLAR_ASSETS_ANNUAL
            else:
                raise ValueError("Invalid value for time period %s " % period)
        else:
            raise ValueError("Invalid value for API %s " % api)

        return resourceid
