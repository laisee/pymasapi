import pytest

try:
    import src.client as client
except (ImportError, ModuleNotFoundError) as err:
    try:
        import pymasapi.src.client as client
    except (ImportError, ModuleNotFoundError) as err:
        print("helper module not found at level")


class Test_FXRates_Average:
    def setup_class(cls):
        cls.c = client.Client()

    def teardown_method(cls):
        cls.c = None

    @pytest.mark.parametrize("period,limit", [("w", 5), ("m", 5), ("y", 5)],  ids=['Weekly', 'Monthly', 'Yearly'])
    def test_fx_rates_average(cls, period, limit):
        ''' testing average weekly/monthly/annual fx rates '''
        data = cls.c.exchange_rates_average(period, limit)
        assert data is not None, "data should not be None"
