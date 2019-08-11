from unittest import TestCase
import pymasapi.client as client
import nose
from nose.tools import ok_


class TestPyMASAPISGXST(TestCase):

    c =  client.Client()

    @classmethod
    def setup(cls):
        print( "executing test setup!")

    @classmethod
    def teardown(cls):
        print("executing test teardown!")

    @classmethod
    def test_credit_card_monthly(cls):
        ''' testing monthly SGX-ST stats '''
        data = cls.c.sgxst("m", 5)
        ok_(data is not None, "data should not be None")

    @classmethod
    def test_credit_card_annual(cls):
        ''' testing annual SGX-ST stats

        Args:
            None

        Returns:
            None
        '''
        data = cls.c.sgxst("y", 5)
        ok_(data is not None, "data should not be None")


if __name__ == '__main__':
    nose.runmodule()
