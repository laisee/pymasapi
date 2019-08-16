from pymasapi.settings import Settings as set

def test_BASEURL():
    '''
    testing BASEURL

    :type foo: integer or None
    :return: None

    '''
    assert set.BASE_URL is not None, "BASE URL is not set"
