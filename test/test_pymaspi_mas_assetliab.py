import pytest

try:
    import src.client as client
except (ImportError, ModuleNotFoundError) as err:
    print(err)
    try:
        import pymasapi.src.client as client
    except (ImportError, ModuleNotFoundError) as err:
        print(err)
        print("helper module not found at level")


class Test_Asset_Liability:
    def setup_class(cls):
        cls.c = client.Client()

    def teardown_method(cls):
        cls.c = None

    @pytest.mark.parametrize(
        "period,limit", [("m", 5), ("y", 5)], ids=["Monthly", "Yearly"]
    )
    def test_mas_asset_liability(cls, period, limit):
        """testing monthly/annual MAS Asset/Liability stats"""
        data = cls.c.mas_asset_liability(period, limit)
        assert data is not None, "data should not be None"
