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

    def test_interest_rates_monthly(cls):
        ''' Method for testing monthly interest_rates '''
        data = cls.c.interest_rates("m", 5) 
        print data
        ok_(data is None,"data should not be None")

    def test_interest_rates_weekly(cls):
        ''' Method for testing weekly interest_rates '''
        data = cls.c.interest_rates("w", 5) 
        print data
        ok_(data is None,"data should not be None")

    def test_interest_rates_annual(cls):
        ''' Method for testing annual interest_rates '''
        data = cls.c.interest_rates("y", 5) 
        ok_(data is None,"data should not be None")

if __name__ == '__main__':
    nose.runmodule()
