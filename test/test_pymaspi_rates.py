from nose.tools import *
import pymaspi.settings as settings
import pymaspi.client as client
import nose

class TestPyMASAPI:

    def setup(cls):
        print "executing test setup!"
        cls.c = client.Client()

    def teardown(cls):
        print "executing test teardown!"
        cls.c = None

    def test_interest_rates_fin_monthly(cls):
        ''' Method for testing monthly finance interest_rates '''
        data = cls.c.interest_rates("fin", "m", 5) 
        ok_(data is None,"data should not be None")

    def test_interest_rates_fin_annual(cls):
        ''' Method for testing annual finance interest_rates '''
        data = cls.c.interest_rates("fin", "y", 5) 
        ok_(data is None,"data should not be None")

    def test_interest_rates_dom_weekly(cls):
        ''' Method for testing weekly interest_rates '''
        data = cls.c.interest_rates("dom", "w", 5) 
        ok_(data is None,"data should not be None")

    def test_interest_rates_dom_monthly(cls):
        ''' Method for testing annual finance interest_rates '''
        data = cls.c.interest_rates("dom", "m", 5) 
        ok_(data is None,"data should not be None")

    def test_interest_rates_dom_annual(cls):
        ''' Method for testing annual interest_rates '''
        data = cls.c.interest_rates("dom", "y", 5) 
        ok_(data is None,"data should not be None")

if __name__ == '__main__':
    nose.runmodule()
