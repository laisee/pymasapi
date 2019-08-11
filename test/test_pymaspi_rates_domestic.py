from unittest import TestCase
import pymasapi.client as client
import nose
from nose.tools import ok_


class TestPyMASAPIRatesDomestic(TestCase):

    c = client.Client()

    @classmethod
    def setup(cls):
        print( "executing test setup!")

    @classmethod
    def teardown(cls):
        print( "executing test teardown!")
        cls.c = None

    @classmethod
    def test_interest_rates_dom_weekly(cls):
        ''' testing weekly interest rates '''
        data = cls.c.interest_rates("w", 5, "dom")
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_interest_rates_dom_monthly(cls):
        ''' testing monthly domestic finance interest rates '''
        data = cls.c.interest_rates("m", 5, "dom")
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_interest_rates_dom_annual(cls):
        ''' testing annual domestic interest_rates '''
        data = cls.c.interest_rates("y", 5, "dom")
        ok_(data is not None, "data should not be None")


if __name__ == '__main__':
    nose.runmodule()
