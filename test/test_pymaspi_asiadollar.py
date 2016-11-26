from unittest import TestCase
import pymaspi.client as client
from nose.tools import ok_
import nose


class TestPyMASAPIAsiaDollarAssets(TestCase):

    c = client.Client()

    @classmethod
    def setup(cls):
        print "executing test setup!"

    @classmethod
    def teardown(cls):
        print "executing test teardown!"
        cls.c = None

    @classmethod
    def test_asian_dollar_assets_monthly(cls):
        ''' Method for testing monthly asian dollar asset stats '''
        data = cls.c.asian_dollar_assets("m", 5)
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_asian_dollar_assetsannual(cls):
        ''' Method for testing annual asian dollar asset stats '''
        data = cls.c.asian_dollar_assets("y", 5)
        ok_(data is not None, "data should not be None")


if __name__ == '__main__':
    nose.runmodule()
