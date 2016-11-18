from nose.tools import *
import pymaspi.settings as settings
import pymaspi.client as client
import nose

class TestPyMASAPI_Money_Supply_DBU:

    def setup(cls):
        print "executing Money Supply DBU test setup!"
        cls.c = client.Client()

    def teardown(cls):
        print "executing Money Supply DBU test teardown!"
        cls.c = None

    def test_money_supply_dbu_monthly(cls):
        ''' Method for testing monthly money supply DBU '''
        data = cls.c.money_supply_dbu("m", 5) 
        ok_(data is None,"data should not be None")

    def test_money_supply_dbu_annual(cls):
        ''' Method for testing annual money supply DBU '''
        data = cls.c.money_supply_dbu("y", 5) 
        ok_(data is None,"data should not be None")

if __name__ == '__main__':
    nose.runmodule()
