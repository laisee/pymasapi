import pymasapi.client as client


def test_fx_rates_end_monthl():
    c = client.Client()
    ''' testing month end  fx rates '''
    data = c.exchange_rates_end("m", 5)
    assert data is not None, "data should not be None"

def test_fx_rates_end_weekly():
    ''' testing week end fx rates '''
    c = client.Client()
    data = c.exchange_rates_end("w", 5)
    assert data is not None, "data should not be None"

def test_fx_rates_end_annual():
    ''' testing year end fx rates '''
    c = client.Client()
    data = c.exchange_rates_end("y", 5)
    assert data is not None, "data should not be None"
