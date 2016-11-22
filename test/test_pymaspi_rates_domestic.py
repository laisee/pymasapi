from unittest import TestCase
import pymaspi.client as client
import nose
from nose.tools import ok_


class TestPyMASAPIRatesDomestic(TestCase):

    @classmethod
    def setup(cls):
        print "executing test setup!"
        cls.c = client.Client()

    @classmethod
    def teardown(cls):
        print "executing test teardown!"
        cls.c = None

    @classmethod
    def test_interest_rates_dom_weekly(cls):
        ''' Method for testing weekly interest rates '''
        data = cls.c.interest_rates("dom", "w", 5)
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_interest_rates_dom_monthly(cls):
        ''' Method for testing monthly domestic finance interest rates '''
        data = cls.c.interest_rates("dom", "m", 5)
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_interest_rates_dom_annual(cls):
        ''' Method for testing annual domestic interest_rates '''
        data = cls.c.interest_rates("dom", "y", 5)
        ok_(data is not None, "data should not be None")


if __name__ == '__main__':
    nose.runmodule()
