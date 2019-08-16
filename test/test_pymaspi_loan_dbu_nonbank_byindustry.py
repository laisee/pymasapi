import pymasapi.client as client

def test_loan_dbu_nonbank_byindustry_monthly():
    c = client.Client()
    ''' testing monthly Loans DBU NonBank stats '''
    data = c.loan_dbu_nonbank_byindustry("m", 5)
    assert data is not None, "data should not be None"

def test_loan_dbu_nonbanky_byindustry_annual():
    c = client.Client()
    ''' testing annual Loans DBU NonBank stats '''
    data = c.loan_dbu_nonbank_byindustry("y", 5)
    assert data is not None, "data should not be None"
