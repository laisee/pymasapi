from nose.tools import *
from unittest import TestCase
import pymaspi.settings as settings
import pymaspi.client as client
import nose

class TestPyMASAPILoanDBUNonBank(TestCase):

    c = client.Client()

    @classmethod
    def setup(cls):
        print "executing test setup!"
        cls.c = client.Client()

    @classmethod
    def teardown(cls):
        print "executing test teardown!"
        cls.c = None

    @classmethod
    def test_loan_dbu_nonbank_byindustry_monthly(cls):
        ''' Method for testing monthly Loans DBU NonBank stats '''
        data = cls.c.loan_dbu_nonbank_byindustry("m", 5) 
        ok_(data is not None,"data should not be None")

    @classmethod
    def test_loan_dbu_nonbanky_byindustry_annual(cls):
        ''' Method for testing annual Loans DBU NonBank stats '''
        data = cls.c.loan_dbu_nonbank_byindustry("y", 5) 
        ok_(data is not None,"data should not be None")

if __name__ == '__main__':
    nose.runmodule()
