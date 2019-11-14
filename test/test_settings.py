from pymasapi.settings import Settings as set


class Test_Settings:
    def test_BASEURL(cls):
        '''
        testing BASEURL
        '''
        assert set.BASE_URL is not None, "BASE URL is not set"
