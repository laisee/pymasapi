import pytest

try:
    import src.client as client
except (ImportError, ModuleNotFoundError) as err:
    try:
        import pymasapi.src.client as client
    except (ImportError, ModuleNotFoundError) as err:
        print("helper module not found at level")


class Test_Money_Supply:
    def setup_class(cls):
        cls.c = client.Client()

    def teardown_method(cls):
        cls.c = None

    @pytest.mark.parametrize("period,limit", [("m", 5), ("y", 5)], ids=['Monthly', 'Yearly'])
    def test_money_supply_dbu(cls, period, limit):
        ''' testing monthly/annual money supply DBU '''
        data = cls.c.money_supply_dbu(period, limit)
        assert data is not None, "data should not be None"
