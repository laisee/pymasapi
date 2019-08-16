import pymasapi.client as client

def test_mas_asset_liability_monthly():
    c = client.Client()
    ''' testing monthly MAS Asset/Liability stats '''
    data = c.mas_asset_liability("m", 5)
    assert data is not None, "data should not be None"

def test_mas_asset_liability_annual():
    c = client.Client()
    ''' testing annual MAS Asset/Liability stats '''
    data = c.mas_asset_liability("y", 5)
    assert data is not None, "data should not be None"
