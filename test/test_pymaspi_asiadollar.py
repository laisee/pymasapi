import pymasapi.client as client

class Test_AsianDollarAssets:

    def test_asian_dollar_assets_monthly(cls):
        c = client.Client()
        ''' testing monthly asian dollar asset stats '''
        data = c.asian_dollar_assets("m", 5)
        assert data is not None, "data should not be None"

    def test_asian_dollar_assetsannual(cls):
        c = client.Client()
        ''' testing annual asian dollar asset stats '''
        data = c.asian_dollar_assets("y", 5)
        assert data is not None, "data should not be None"
