import pymasapi.client as client

def test_credit_card_monthly():
    c =  client.Client()
    ''' testing monthly SGX-ST stats '''
    data = c.sgxst("m", 5)
    assert data is not None, "data should not be None"

def test_credit_card_annual():
    c =  client.Client()
    ''' testing annual SGX-ST stats

    Args:
        None

    Returns:
        None
    '''
    data = c.sgxst("y", 5)
    assert data is not None, "data should not be None"
