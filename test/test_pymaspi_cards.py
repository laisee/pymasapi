import pytest
import pymasapi.client as client

class Test_Cards:

    def setup_class(cls):
        cls.c = client.Client()

    def teardown_method(cls):
        cls.c = None

    @pytest.mark.parametrize("period,limit", [("m",5), ("y",5)])
    def test_credit_card(cls, period, limit):
        ''' testing monthly credit card stats '''
        data = cls.c.credit_card("m", 5)
        assert data is not None, "data should not be None"
