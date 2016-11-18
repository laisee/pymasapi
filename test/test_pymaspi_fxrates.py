from nose.tools import *
import pymaspi.settings as settings
import pymaspi.client as client
import nose

class TestPyMASAPI:

    def setup(cls):
        print "executing fxrates test setup!"
        cls.c = client.Client()

    def teardown(cls):
        print "executing fxrates test teardown!"
        cls.c = None

    def test_fx_rates_average_monthly(cls):
        ''' Method for testing average monthly fx rates '''
        data = cls.c.exchange_rates_average("m", 5) 
        ok_(data is not None,"data should not be None")

    def test_fx_rates_average_weekly(cls):
        ''' Method for testing average weekly fx rates '''
        data = cls.c.exchange_rates_average("w", 5) 
        ok_(data is not None,"data should not be None")

    def test_fx_rates_average_annual(cls):
        ''' Method for testing average annual fx rates '''
        data = cls.c.exchange_rates_average("y", 5) 
        ok_(data is not None,"data should not be None")

    def test_fx_rates_end_monthl(cls):
        ''' Method for testing month end  fx rates '''
        data = cls.c.exchange_rates_end("m", 5) 
        ok_(data is not None,"data should not be None")

    def test_fx_rates_end_weekly(cls):
        ''' Method for testing week end fx rates '''
        data = cls.c.exchange_rates_end("w", 5) 
        ok_(data is not None,"data should not be None")

    def test_fx_rates_end_annual(cls):
        ''' Method for testing year end fx rates '''
        data = cls.c.exchange_rates_end("y", 5) 
        ok_(data is not None,"data should not be None")

if __name__ == '__main__':
    nose.runmodule()
