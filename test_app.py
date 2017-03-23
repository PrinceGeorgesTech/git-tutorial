from app import app
import pytest

@pytest.fixture()
def app_instance():
    yield app.test_client() 


class TestRoutes:
    def test_root_route_works(self, app_instance):
        url_paths = [url.rule for url in app.url_map.iter_rules() if 'static' not in url.rule]
        for url in url_paths:
            assert app_instance.get(url).status_code == 200

