from nose.tools import *
from unittest import TestCase
import pymaspi.settings as settings

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
        ''' Method for testing BASEURL '''
        ok_(settings.BASE_URL is not None, "BASE URL should not equal None! : %s" % settings.BASE_URL)

if __name__ == '__main__':
    nose.runmodule()
