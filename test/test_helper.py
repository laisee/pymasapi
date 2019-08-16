from pymasapi.helper import apply_format, apply_format_level, get_datetime, get_timestamp, get_response,  guard
from requests.exceptions import HTTPError
import pytest

class Test_Helper:

    def test_apply_format(cls):
        '''
        testing helper::apply_format
    
        :return: None
        '''
        assert apply_format(88.1234567)  == "88.12346", "method apply_format() result is not correct: %s " % apply_format(88.1234567)
    
    def test_apply_format_level(cls):
        '''
        testing helper::apply_format_level
    
        :return: None
        '''
        assert apply_format_level(88.1234567)  == "88.12", "method apply_format_level() result is not correct: %s " % apply_format_level(88.12345)
    
    def test_get_datetime(cls):
        '''
        testing helper::get_datetime
    
        :return: None
    
        '''
        assert get_datetime() is not None, "method get_datetime() response is not valid"
    
    
    def test_get_timestamp(cls):
        '''
        testing helper::get_timestamp
    
        :return: None
        '''
        assert get_timestamp() is not None, "method get_timestamp() response is not valid"
    
    def test_guard_success(cls):
        '''
        testing helper::guard(success)
    
        :return: None
    
        '''
        assert guard("resourceid", "https://dev.null/?and1") is None, "method guard() response is not valid"
    
    def test_guard_fail_resourceid(cls):
        '''
        testing helper::guard(resourceid.fail)
    
        :return: None
    
        '''
        with pytest.raises(ValueError) as e:
            guard(None, "https://dev.null/?and1")
    
        assert "ValueError" in str(e)
        assert e.type == ValueError

    def test_guard_fail_url(cls):
        '''
        testing helper::guard(url.fail)
    
        :return: None
    
        '''
        with pytest.raises(ValueError) as e:
            guard(None, "https://dev.null/?and1")
        assert "ValueError" in str(e)
        assert e.type == ValueError
    
    def test_get_response_fail_resourceid(cls):
        '''
        testing helper::get_response(fail.resourceid)
    
        :return: None
    
        '''
        with pytest.raises(ValueError) as e:
            get_response("url", None)
        assert "ValueError" in str(e)
        assert e.type == ValueError
    
    def test_get_response_fail_url(cls):
        '''
        testing helper::get_response(fail.url)
    
        :return: None
    
        '''
        with pytest.raises(ValueError) as e:
            get_response(None, "resourceid")
        assert "ValueError" in str(e)
        assert e.type == ValueError
    
    def test_get_response_success_url(cls):
        '''
        testing helper::get_response(success.url)
    
        :return: json
    
        '''
        resp = get_response("https://api.github.com/search/repositories?q=%s", "xrp")
        assert resp is not None
    
    def test_get_response_fail_url(cls):
        '''
        testing helper::get_response(fail.url)
    
        :return: json
    
        '''
        with pytest.raises(HTTPError) as e:
            get_response("https://zzz.github.com/search/repositories?q=%s", "xrp")
        assert "HTTPError" in str(e)
        assert e.type == HTTPError
