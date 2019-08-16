import pymasapi.client as client

def test_fx_rates_average_monthly():
    ''' testing average monthly fx rates '''
    c = client.Client()
    data = c.exchange_rates_average("m", 5)
    assert data is not None, "data should not be None"

def test_fx_rates_average_weekly():
    ''' testing average weekly fx rates '''
    c = client.Client()
    data = c.exchange_rates_average("w", 5)
    assert data is not None, "data should not be None"

def test_fx_rates_average_annual():
    ''' testing average annual fx rates '''
    c = client.Client()
    data = c.exchange_rates_average("y", 5)
    assert data is not None, "data should not be None"
