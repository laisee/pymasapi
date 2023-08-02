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


class Test_Loan_Finance:
    def setup_class(cls):
        cls.client = client.Client()

    def teardown_method(cls):
        cls.client = None

    @pytest.mark.parametrize(
        "period,limit", [("m", 5), ("y", 5)], ids=["Monthly", "Yearly"]
    )
    def test_loan_finance(cls, period, limit):
        """testing monthly/annual Loans Finance stats"""
        data = cls.client.loan_finance(period, limit)
        assert data is not None, "data should not be None"
