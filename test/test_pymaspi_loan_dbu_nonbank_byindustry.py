from unittest import TestCase
import pymasapi.client as client
import nose
from nose.tools import ok_


class TestPyMASAPILoanDBUNonBank(TestCase):

    c = client.Client()

    @classmethod
    def setup(cls):
        print( "executing test setup!")
        cls.c = client.Client()

    @classmethod
    def teardown(cls):
        print( "executing test teardown!")
        cls.c = None

    @classmethod
    def test_loan_dbu_nonbank_byindustry_monthly(cls):
        ''' testing monthly Loans DBU NonBank stats '''
        data = cls.c.loan_dbu_nonbank_byindustry("m", 5)
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_loan_dbu_nonbanky_byindustry_annual(cls):
        ''' testing annual Loans DBU NonBank stats '''
        data = cls.c.loan_dbu_nonbank_byindustry("y", 5)
        ok_(data is not None, "data should not be None")


if __name__ == '__main__':
    nose.runmodule()
