import importlib.util
import os
import pytest


def _load_generate_sitemap():
    script_path = os.path.join(
        os.path.dirname(__file__), "..", "scripts", "generate-sitemap.py"
    )
    spec = importlib.util.spec_from_file_location("generate_sitemap", script_path)
    mod = importlib.util.module_from_spec(spec)
    # Load the module from its file path (required because filename contains a hyphen)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="session")
def sitemap_module():
    return _load_generate_sitemap()


@pytest.fixture(scope="session")
def find_pages(sitemap_module):
    return sitemap_module.find_pages


@pytest.fixture(scope="session")
def derive_url(sitemap_module):
    return sitemap_module.derive_url


@pytest.fixture(scope="session")
def get_heuristics(sitemap_module):
    return sitemap_module.get_heuristics


@pytest.fixture(scope="session")
def generate_sitemap(sitemap_module):
    return sitemap_module.generate_sitemap
