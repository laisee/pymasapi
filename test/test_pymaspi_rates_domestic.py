import pytest
import pymasapi.client as client

class Test_Interest_Rates_Domestic:

    def setup_class(cls):
        cls.c = client.Client()

    def teardown_method(cls):
        cls.c = None

    @pytest.mark.parametrize("period,limit", [("w",5), ("m",5), ("y",5)])
    def test_interest_rates_dom(cls, period, limit):
        ''' testing weekly/monthly/annual interest rates '''
        data = cls.c.interest_rates(period, limit, "dom")
        assert data is not None, "data should not be None"
