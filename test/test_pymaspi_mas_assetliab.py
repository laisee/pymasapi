from nose.tools import *
import pymaspi.settings as settings
import pymaspi.client as client
import nose

class TestPyMASAPIMasAseetLiability:

    def setup(cls):
        print "executing test setup!"
        cls.c = client.Client()

    def teardown(cls):
        print "executing test teardown!"
        cls.c = None

    def test_mas_asset_liability_monthly(cls):
        ''' Method for testing monthly MAS Asset/Liability stats '''
        data = cls.c.mas_asset_liability("m", 5) 
        ok_(data is not None,"data should not be None")

    def test_mas_asset_liability_annual(cls):
        ''' Method for testing annual MAS Asset/Liability stats '''
        data = cls.c.mas_asset_liability("y", 5) 
        ok_(data is not None,"data should not be None")

if __name__ == '__main__':
    nose.runmodule()
