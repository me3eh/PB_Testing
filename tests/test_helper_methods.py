from services.helper_methods import get_full_url
import pytest


@pytest.fixture
def full_url():
   return "https://strona.pl/som_endpoint"


@pytest.mark.parametrize("domain, endpoint",
                         [
                             ("https://strona.pl", 'som_endpoint'),
                             ("https://strona.pl", '/som_endpoint'),
                             ("https://strona.pl/", 'som_endpoint')
                          ]
                         )
def test_get_full_url(full_url, domain, endpoint):
    created_url = get_full_url(domain, endpoint)
    assert created_url == full_url
