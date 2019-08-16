import pymasapi.client as client

def test_credit_card_monthly():
    c = client.Client()
    ''' testing monthly credit card stats '''
    data = c.credit_card("m", 5)
    assert(data is not None, "data should not be None")

def test_credit_card_annual():
    c = client.Client()
    ''' testing annual credit card stats '''
    data = c.credit_card("y", 5)
    assert(data is not None, "data should not be None")
