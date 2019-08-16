import pytest
import pymasapi.client as client

class Test_Interest_Rate_Financial:

    def setup_class(cls):
        cls.c = client.Client()

    def teardown_method(cls):
        cls.c = None

    @pytest.mark.parametrize("period,limit", [("m",5), ("y",5)])
    def test_interest_rates_fin(cls, period, limit):
        ''' testing monthly/annual finance interest rates '''
        data = cls.c.interest_rates(period, limit, "fin")
        assert data is not None, "data should not be None"
