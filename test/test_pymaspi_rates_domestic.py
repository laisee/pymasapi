import pymasapi.client as client


def test_interest_rates_dom_weekly():
    c = client.Client()
    ''' testing weekly interest rates '''
    data = c.interest_rates("w", 5, "dom")
    assert data is not None, "data should not be None"

def test_interest_rates_dom_monthly():
    c = client.Client()
    ''' testing monthly domestic finance interest rates '''
    data = c.interest_rates("m", 5, "dom")
    assert data is not None, "data should not be None"

def test_interest_rates_dom_annual():
    c = client.Client()
    ''' testing annual domestic interest_rates '''
    data = c.interest_rates("y", 5, "dom")
    assert data is not None, "data should not be None"
