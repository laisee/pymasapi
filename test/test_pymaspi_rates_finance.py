from unittest import TestCase
import pymasapi.client as client
import nose
from nose.tools import ok_


class TestPyMASAPIRatesFinance(TestCase):

    c = client.Client()

    @classmethod
    def setup(cls):
        print( "executing test setup!")
        cls.c = client.Client()

    @classmethod
    def teardown(cls):
        print( "executing test teardown!")
        cls.c = None

    @classmethod
    def test_interest_rates_fin_monthly(cls):
        ''' testing monthly finance interest rates '''
        data = cls.c.interest_rates("m", 5, "fin")
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_interest_rates_fin_annual(cls):
        ''' testing annual finance interest rates '''
        data = cls.c.interest_rates("y", 5, "fin")
        ok_(data is not None, "data should not be None")


if __name__ == '__main__':
    nose.runmodule()
