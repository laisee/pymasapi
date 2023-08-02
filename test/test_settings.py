try:
    from src.settings import Settings
except (ImportError, ModuleNotFoundError) as err:
    try:
        from pymasapi.src.settings import Settings
    except (ImportError, ModuleNotFoundError) as err:
        print("Settings module not found at level")


class Test_Settings:
    def test_BASEURL(cls):
        '''
        testing BASEURL
        '''
        assert Settings.BASE_URL is not None, "BASE URL is not set"

    def test_BASE_SETTINGS(cls):
        '''
        testing BASEURL
        '''
        assert Settings is not None, "Settings class is not available"
