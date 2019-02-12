import nose
from nose.tools import ok_
from unittest import TestCase
import pymasapi.client as client


class TestPyMASAPIDepositsDBUNonBank(TestCase):

    c = client.Client()

    @classmethod
    def setup(cls):
        print( "executing test setup!")

    @classmethod
    def teardown(cls):
        print( "executing test teardown!")
        cls.c = None

    @classmethod
    def test_deposits_dbu_nonbank_monthly(cls):
        ''' Method for testing monthly Deposits DBU NonBank stats '''
        data = cls.c.mas_asset_liability("m", 5)
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_deposits_dbu_nonbanky_annual(cls):
        ''' Method for testing annual Deposits DBU NonBank stats '''
        data = cls.c.mas_asset_liability("y", 5)
        ok_(data is not None, "data should not be None")


if __name__ == '__main__':
    nose.runmodule()
