from unittest import TestCase
import pymaspi.client as client
import nose
from nose.tools import ok_


class TestPyMASAPIRatesFinance(TestCase):

    c = client.Client()

    @classmethod
    def setup(cls):
        print "executing test setup!"
        cls.c = client.Client()

    @classmethod
    def teardown(cls):
        print "executing test teardown!"
        cls.c = None

    @classmethod
    def test_interest_rates_fin_monthly(cls):
        ''' Method for testing monthly finance interest rates '''
        data = cls.c.interest_rates("fin", "m", 5)
        print data
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_interest_rates_fin_annual(cls):
        ''' Method for testing annual finance interest rates '''
        data = cls.c.interest_rates("fin", "y", 5)
        ok_(data is not None, "data should not be None")


if __name__ == '__main__':
    nose.runmodule()
