from unittest import TestCase
from nose.tools import ok_
from pymasapi.settings import Settings as set
import nose


class TESTPyMASAPISettings(TestCase):

    @classmethod
    def setup(cls):
        print("executing test setup!")
        print("base URL : ", set.BASE_URL)

    @classmethod
    def teardown(cls):
        print("executing test teardown!")

    @classmethod
    def test_BASEURL(cls):
        '''
        Method for testing BASEURL

        :type foo: integer or None
        :return: None

        '''
        ok_(set.BASE_URL is not None, "BASE URL is not set")


if __name__ == '__main__':
    nose.runmodule()
