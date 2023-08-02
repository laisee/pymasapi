import pytest

try:
    import src.client as client
except (ImportError, ModuleNotFoundError) as err:
    try:
        import pymasapi.src.client as client
    except (ImportError, ModuleNotFoundError) as err:
        print("helper module not found at level")


class Test_Credit_Card:
    def setup_class(cls):
        cls.c = client.Client()

    def teardown_method(cls):
        cls.c = None

    @pytest.mark.parametrize("period,limit", [("m", 5), ("y", 5)], ids=['Monthly', 'Yearly'])
    def test_credit_card(cls, period, limit):
        ''' testing monthly/annual SGX-ST stats '''
        data = cls.c.sgxst(period, limit)
        assert data is not None, "data should not be None"
