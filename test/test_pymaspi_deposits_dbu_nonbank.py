import pytest
import pymasapi.client as client


class Test_Deposits:
    def setup_class(cls):
        cls.c = client.Client()

    def teardown_method(cls):
        cls.c = None

    @pytest.mark.parametrize("period,limit", [("m", 5), ("y", 5)])
    def test_deposits_dbu_nonbank(cls, period, limit):
        ''' testing monthly/yearly Deposits DBU NonBank stats '''
        data = cls.c.deposits_dbu_nonbank(period, limit)
        assert data is not None, "data should not be None"
