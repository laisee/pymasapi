import pymasapi.client as client

def test_loan_acu_nonbank_byindustry_monthly():
    ''' testing monthly Loans DBU NonBank stats '''
    c = client.Client()
    data = c.loan_acu_nonbank_byindustry("m", 5)
    assert data is not None, "data should not be None"

def test_loan_acu_nonbanky_byindustry_annual():
    ''' testing annual Loans DBU NonBank stats '''
    c = client.Client()
    data = c.loan_acu_nonbank_byindustry("y", 5)
    assert data is not None, "data should not be None"
