from unittest import TestCase
import pymasapi.client as client
import nose
from nose.tools import ok_


class TestPyMASAPIAverage(TestCase):

    c = client.Client()

    @classmethod
    def setup(cls):
        print( "executing fxrates test setup!")

    @classmethod
    def teardown(cls):
        print( "executing fxrates test teardown!")
        cls.c = None

    @classmethod
    def test_fx_rates_average_monthly(cls):
        ''' Method for testing average monthly fx rates '''
        data = cls.c.exchange_rates_average("m", 5)
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_fx_rates_average_weekly(cls):
        ''' Method for testing average weekly fx rates '''
        data = cls.c.exchange_rates_average("w", 5)
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_fx_rates_average_annual(cls):
        ''' Method for testing average annual fx rates '''
        data = cls.c.exchange_rates_average("y", 5)
        ok_(data is not None, "data should not be None")


if __name__ == '__main__':
    nose.runmodule()
