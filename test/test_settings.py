from unittest import TestCase
import pymaspi.settings as settings
from nose.tools import ok_
import nose


class TESTPyMASAPISettings(TestCase):

    @classmethod
    def setup(cls):
        print "executing test setup!"
        print "base URL : ", settings.BASE_URL

    @classmethod
    def teardown(cls):
        print "executing test teardown!"

    @classmethod
    def test_BASEURL(cls):
        '''
        Method for testing BASEURL

        :type foo: integer or None
        :return: None

        '''
        ok_(settings.BASE_URL is not None, "BASE URL is not set")


if __name__ == '__main__':
    nose.runmodule()
