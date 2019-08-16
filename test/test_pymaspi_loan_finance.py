import pytest
import pymasapi.client as client

class Test_Loan_Finance:

    def setup_class(cls):
        cls.c = client.Client()

    def teardown_method(cls):
        cls.c = None

    @pytest.mark.parametrize("period,limit", [("m",5), ("y",5)])
    def test_loan_finance(cls,period, limit):
        ''' testing monthly/annual Loans Finance stats '''
        data = cls.c.loan_finance(period, limit)
        assert data is not None, "data should not be None"
