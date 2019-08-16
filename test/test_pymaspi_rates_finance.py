import pymasapi.client as client

def test_interest_rates_fin_monthly():
    c = client.Client()
    ''' testing monthly finance interest rates '''
    data = c.interest_rates("m", 5, "fin")
    assert data is not None, "data should not be None"

def test_interest_rates_fin_annual():
    ''' testing annual finance interest rates '''
    c = client.Client()
    data = c.interest_rates("y", 5, "fin")
    assert data is not None, "data should not be None"
