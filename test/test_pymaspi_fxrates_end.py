import pytest

try:
    import src.client as client
except (ImportError, ModuleNotFoundError) as err:
    try:
        import pymasapi.src.client as client
    except (ImportError, ModuleNotFoundError) as err:
        print("helper module not found at level")


class Test_FXRates_End:
    def setup_class(cls):
        cls.c = client.Client()

    def teardown_method(cls):
        cls.c = None

    @pytest.mark.parametrize("period,limit", [("w", 5), ("m", 5), ("y", 5)], ids=['Weekly', 'Monthly', 'Yearly'])
    def test_fx_rates_end(cls, period, limit):
        ''' testing month end  fx rates '''
        data = cls.c.exchange_rates_end(period, limit)
        assert data is not None, "data should not be None"
