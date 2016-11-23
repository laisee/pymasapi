from unittest import TestCase
import pymaspi.client as client
import nose
from nose.tools import ok_


class TestPyMASAPILoanFinance(TestCase):

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
    def test_loan_finance_monthly(cls):
        ''' Method for testing monthly Loans Finance stats '''
        data = cls.c.loan_finance("m", 5)
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_loan_finance_annual(cls):
        ''' Method for testing annual Loans Finance stats '''
        data = cls.c.loan_finance("y", 5)
        ok_(data is not None, "data should not be None")


if __name__ == '__main__':
    nose.runmodule()
