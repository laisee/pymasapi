from unittest import TestCase
import pymaspi.client as client
import nose
from nose.tools import ok_


class TestPyMASAPIFXEnd(TestCase):

    c = client.Client()

    @classmethod
    def setup(cls):
        print "executing fxrates test setup!"

    @classmethod
    def teardown(cls):
        print "executing fxrates test teardown!"
        cls.c = None

    @classmethod
    def test_fx_rates_end_monthl(cls):
        ''' Method for testing month end  fx rates '''
        data = cls.c.exchange_rates_end("m", 5)
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_fx_rates_end_weekly(cls):
        ''' Method for testing week end fx rates '''
        data = cls.c.exchange_rates_end("w", 5)
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_fx_rates_end_annual(cls):
        ''' Method for testing year end fx rates '''
        data = cls.c.exchange_rates_end("y", 5)
        ok_(data is not None, "data should not be None")


if __name__ == '__main__':
    nose.runmodule()
