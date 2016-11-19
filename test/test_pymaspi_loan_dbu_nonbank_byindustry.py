from nose.tools import *
import pymaspi.settings as settings
import pymaspi.client as client
import nose

class TestPyMASAPILoanDBUNonBank:

    def setup(cls):
        print "executing test setup!"
        cls.c = client.Client()

    def teardown(cls):
        print "executing test teardown!"
        cls.c = None

    def test_loan_dbu_nonbank_byindustry_monthly(cls):
        ''' Method for testing monthly Loans DBU NonBank stats '''
        data = cls.c.loan_dbu_nonbank_byindustry("m", 5) 
        ok_(data is not None,"data should not be None")

    def test_loan_dbu_nonbanky_byindustry_annual(cls):
        ''' Method for testing annual Loans DBU NonBank stats '''
        data = cls.c.loan_dbu_nonbank_byindustry("y", 5) 
        ok_(data is not None,"data should not be None")

if __name__ == '__main__':
    nose.runmodule()
