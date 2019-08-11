from unittest import TestCase
from nose.tools import *
from pymasapi.helper import apply_format, apply_format_level, get_datetime, get_timestamp, get_response,  guard
from requests.exceptions import HTTPError

import nose


class TestPyMASAPIHelper(TestCase):

    @classmethod
    def setup(cls):
        print("executing test setup!")

    @classmethod
    def teardown(cls):
        print("executing test teardown!")

    @classmethod
    def test_apply_format(cls):
        '''
        testing helper::apply_format

        :return: None

        '''
        ok_(apply_format(88.1234567)  == "88.12346", "method apply_format() result is not correct: %s " % apply_format(88.1234567))

    @classmethod
    def test_apply_format_level(cls):
        '''
        testing helper::apply_format_level

        :return: None

        '''
        ok_(apply_format_level(88.1234567)  == "88.12", "method apply_format_level() result is not correct: %s " % apply_format_level(88.12345))

    @classmethod
    def test_get_datetime(cls):
        '''
        testing helper::get_datetime

        :return: None

        '''
        ok_(get_datetime() is not None, "method get_datetime() response is not valid")


    @classmethod
    def test_get_timestamp(cls):
        '''
        testing helper::get_timestamp

        :return: None

        '''
        ok_(get_timestamp() is not None, "method get_timestamp() response is not valid")

    @classmethod
    def test_guard_success(cls):
        '''
        testing helper::guard(success)

        :return: None

        '''
        ok_(guard("resourceid", "https://dev.null/?and1") is None, "method guard() response is not valid")

    @classmethod
    @raises(ValueError)
    def test_guard_fail_resourceid(cls):
        '''
        testing helper::guard(resourceid.fail)

        :return: None

        '''
        ok_(guard(None, "https://dev.null/?and1") is None, "method guard() response is not valid")

    @classmethod
    @raises(ValueError)
    def test_guard_fail_url(cls):
        '''
        testing helper::guard(url.fail)

        :return: None

        '''
        ok_(guard(None, "https://dev.null/?and1") is None, "method guard() response is not valid")

    @classmethod
    @raises(ValueError)
    def test_get_response_fail_resourceid(cls):
        '''
        testing helper::get_response(fail.resourceid)

        :return: None

        '''
        ok_(get_response("url", None) is None, "method get_response() response is not valid")

    @classmethod
    @raises(ValueError)
    def test_get_response_fail_url(cls):
        '''
        testing helper::get_response(fail.url)

        :return: None

        '''
        ok_(get_response(None, "resourceid") is None, "method get_response() response is not valid")

    @classmethod
    #@raises(ValueError)
    def test_get_response_success_url(cls):
        '''
        testing helper::get_response(success.url)

        :return: json

        '''
        ok_(get_response("https://api.github.com/search/repositories?q=%s", "xrp") is not None, "method get_response() response is not valid")

    @classmethod
    @raises(HTTPError)
    def test_get_response_fail_url(cls):
        '''
        testing helper::get_response(fail.url)

        :return: json

        '''
        ok_(get_response("https://zzz.github.com/search/repositories?q=%s", "xrp") is None, "method get_response() response is not valid")

if __name__ == '__main__':
    nose.runmodule()
