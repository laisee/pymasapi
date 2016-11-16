from nose.tools import *
import pymaspi.settings as settings

def setup():
    print "executing test setup!"
    print "base URL : ", settings.BASE_URL

def teardown():
    print "executing test teardown!"

def test_BASEURL():
    ''' Method for testing BASEURL '''
    ok_(settings.BASE_URL is not None, "BASE URL should not equal None! : %s" % settings.BASE_URL)

if __name__ == '__main__':
    nose.runmodule()
