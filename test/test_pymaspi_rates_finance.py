import pytest

try:
    import src.client as client
except (ImportError, ModuleNotFoundError) as err:
    try:
        import pymasapi.src.client as client
    except (ImportError, ModuleNotFoundError) as err:
        print("helper module not found at level")


class Test_Interest_Rate_Financial:
    def setup_class(cls):
        cls.c = client.Client()

    def teardown_method(cls):
        cls.c = None

    @pytest.mark.parametrize("period,limit", [("m", 5), ("y", 5)], ids=['Monthly', 'Yearly'])
    def test_interest_rates_fin(cls, period, limit):
        ''' testing monthly/annual finance interest rates '''
        data = cls.c.interest_rates(period, limit, "fin")
        assert data is not None, "data should not be None"
