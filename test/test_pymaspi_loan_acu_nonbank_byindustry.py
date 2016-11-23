from unittest import TestCase
import pymaspi.client as client
import nose
from nose.tools import ok_


class TestPyMASAPILoanACUNonBank(TestCase):

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
    def test_loan_acu_nonbank_byindustry_monthly(cls):
        ''' Method for testing monthly Loans DBU NonBank stats '''
        data = cls.c.loan_acu_nonbank_byindustry("m", 5)
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_loan_acu_nonbanky_byindustry_annual(cls):
        ''' Method for testing annual Loans DBU NonBank stats '''
        data = cls.c.loan_acu_nonbank_byindustry("y", 5)
        ok_(data is not None, "data should not be None")


if __name__ == '__main__':
    nose.runmodule()
