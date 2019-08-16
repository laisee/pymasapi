import pymasapi.client as client


def test_asian_dollar_assets_monthly():
    c = client.Client()
    ''' testing monthly asian dollar asset stats '''
    data = c.asian_dollar_assets("m", 5)
    assert data is not None, "data should not be None"

def test_asian_dollar_assetsannual():
    c = client.Client()
    ''' testing annual asian dollar asset stats '''
    data = c.asian_dollar_assets("y", 5)
    assert data is not None, "data should not be None"
