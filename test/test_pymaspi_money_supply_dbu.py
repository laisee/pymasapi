import pymasapi.client as client

def test_money_supply_dbu_monthly():
    c = client.Client()
    ''' testing monthly money supply DBU '''
    data = c.money_supply_dbu("m", 5)
    assert data is not None, "data should not be None"

def test_money_supply_dbu_annual():
    c = client.Client()
    ''' testing annual money supply DBU '''
    data = c.money_supply_dbu("y", 5)
    assert data is not None, "data should not be None"
