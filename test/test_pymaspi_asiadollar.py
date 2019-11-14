import pytest
import pymasapi.client as client


class Test_AsianDollarAssets:
    def setup_class(cls):
        cls.c = client.Client()

    def teardown_method(cls):
        cls.c = None

    @pytest.mark.parametrize("period,limit", [("m", 5), ("y", 5)])
    def test_asian_dollar_assets(cls, period, limit):
        ''' testing asian dollar asset stats '''
        data = cls.c.asian_dollar_assets(period, limit)
        assert data is not None, "data should not be None"
