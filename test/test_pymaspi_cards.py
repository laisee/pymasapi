from nose.tools import *
from unittest import TestCase
import pymaspi.settings as settings
import pymaspi.client as client
import nose

class TestPyMASAPICards(TestCase):

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
        ''' Method for testing monthly credit card stats '''
        data = cls.c.credit_card("m", 5) 
        ok_(data is not None,"data should not be None")

    @classmethod
    def test_credit_card_annual(cls):
        ''' Method for testing annual credit card stats '''
        data = cls.c.credit_card("y", 5) 
        ok_(data is not None,"data should not be None")

if __name__ == '__main__':
    nose.runmodule()
