import pytest
from requests.exceptions import HTTPError


try:
    from src.client import Client
except (ImportError, ModuleNotFoundError) as err:
    try:
        from pymasapi.src.client import Client
    except (ImportError, ModuleNotFoundError) as err:
        print("helper module not found at level")


class Test_Client:
    def setup_class(cls):
        cls.c = Client()

    def teardown_method(cls):
        cls.c = None

    def test_client_not_none(cls):
        assert cls.c is not None, "Client object should not be None"

    def test_credit_card(cls):
        data = cls.c.credit_card('m')
        assert data is not None, "Client object should not be None"

    @pytest.mark.parametrize(("name"), ["SGXST", "FINLOAN", "ACUNONBANKBYIND", "DBUNONBANKBYIND", "DBUNONBANK", "FXRATESEND", "FXRATESAVG", "RATES", "MONEY", "CCARD", "MASALM", "ADLRASSETS"])
    def test_get_resource_id(cls, name):
        with pytest.raises(ValueError) as exc:
            cls.c.get_resource_id(name, 'z')
