from nose.tools import *
from unittest import TestCase
import pymaspi.settings as settings
import pymaspi.client as client
import nose

class TestPyMASAPISGXST(TestCase):

    c = client.Client()

    @classmethod
    def setup(cls):
        print "executing test setup!"

    @classmethod
    def teardown(cls):
        print "executing test teardown!"
        cls.c = None

    @classmethod
    def test_credit_card_monthly(cls):
        ''' Method for testing monthly SGX-ST stats '''
        data = cls.c.sgxst("m", 5) 
        ok_(data is not None,"data should not be None")

    @classmethod
    def test_credit_card_annual(cls):
        ''' Method for testing annual SGX-ST stats '''
        data = cls.c.sgxst("y", 5) 
        ok_(data is not None,"data should not be None")

if __name__ == '__main__':
    nose.runmodule()
