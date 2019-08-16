import pymasapi.client as client


def test_deposits_dbu_nonbank_monthly():
    c = client.Client()
    ''' testing monthly Deposits DBU NonBank stats '''
    data = c.deposits_dbu_nonbank("m", 5)
    assert data is not None, "data should not be None"

def test_deposits_dbu_nonbanky_annual():
    c = client.Client()
    ''' testing annual Deposits DBU NonBank stats '''
    data = c.deposits_dbu_nonbank("y", 5)
    assert data is not None, "data should not be None"
