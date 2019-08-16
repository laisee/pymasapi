import pymasapi.client as client


def test_loan_finance_monthly():
    c = client.Client()
    ''' testing monthly Loans Finance stats '''
    data = c.loan_finance("m", 5)
    assert data is not None, "data should not be None"

def test_loan_finance_annual():
    c = client.Client()
    ''' testing annual Loans Finance stats '''
    data = c.loan_finance("y", 5)
    assert data is not None, "data should not be None"
