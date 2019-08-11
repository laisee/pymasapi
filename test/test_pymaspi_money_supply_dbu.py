from unittest import TestCase
import pymasapi.client as client
import nose
from nose.tools import ok_


class TestPyMASAPIMoneySupplyDBU(TestCase):

    c = client.Client()

    @classmethod
    def setup(cls):
        print( "executing Money Supply DBU test setup!")
        cls.c = client.Client()

    @classmethod
    def teardown(cls):
        print( "executing Money Supply DBU test teardown!")
        cls.c = None

    @classmethod
    def test_money_supply_dbu_monthly(cls):
        ''' testing monthly money supply DBU '''
        data = cls.c.money_supply_dbu("m", 5)
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_money_supply_dbu_annual(cls):
        ''' testing annual money supply DBU '''
        data = cls.c.money_supply_dbu("y", 5)
        ok_(data is not None, "data should not be None")


if __name__ == '__main__':
    nose.runmodule()
