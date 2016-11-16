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

    def test_interest_rates(cls):
        ''' Method for testing interest_rates '''
        data = cls.c.interest_rates(5) 
        print data
        ok_(data is None,"data should not be None")

if __name__ == '__main__':
    nose.runmodule()
