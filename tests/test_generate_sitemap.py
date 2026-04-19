import os
import pytest


def make_site(tmp_path, files):
    """Create a fake site/ tree. files is a list of relative paths."""
    for rel in files:
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("")
    return tmp_path


def test_find_pages_returns_md_and_html(tmp_path, find_pages):
    site = make_site(tmp_path, ["index.html", "about/index.md", "status.md"])
    result = find_pages(str(site))
    names = {os.path.basename(p) for p in result}
    assert names == {"index.html", "index.md", "status.md"}


def test_find_pages_excludes_img_dir(tmp_path, find_pages):
    site = make_site(tmp_path, ["index.html", "img/logo.svg", "img/favicon/icon.png"])
    result = find_pages(str(site))
    assert all("img" not in p.split(os.sep) for p in result)
    assert len(result) == 1


def test_find_pages_excludes_js_dir(tmp_path, find_pages):
    site = make_site(tmp_path, ["index.html", "js/app.js"])
    result = find_pages(str(site))
    assert all("js" not in p.split(os.sep) for p in result)
    assert len(result) == 1


def test_find_pages_excludes_favicon_dir(tmp_path, find_pages):
    site = make_site(tmp_path, ["index.html", "img/favicon/icon.ico"])
    result = find_pages(str(site))
    assert len(result) == 1


def test_find_pages_ignores_non_page_extensions(tmp_path, find_pages):
    site = make_site(tmp_path, ["index.html", "main.css", "data.toml"])
    result = find_pages(str(site))
    assert len(result) == 1
    assert result[0].endswith("index.html")


def test_derive_url_root_index(tmp_path, derive_url):
    site = str(tmp_path)
    filepath = os.path.join(site, "index.html")
    assert derive_url(filepath, site) == "https://vyos.net/"


def test_derive_url_subdir_index(tmp_path, derive_url):
    site = str(tmp_path)
    filepath = os.path.join(site, "about", "index.md")
    assert derive_url(filepath, site) == "https://vyos.net/about/"


def test_derive_url_regular_md(tmp_path, derive_url):
    site = str(tmp_path)
    filepath = os.path.join(site, "about", "upstream-projects.md")
    assert derive_url(filepath, site) == "https://vyos.net/about/upstream-projects/"


def test_derive_url_top_level_md(tmp_path, derive_url):
    site = str(tmp_path)
    filepath = os.path.join(site, "status.md")
    assert derive_url(filepath, site) == "https://vyos.net/status/"


def test_derive_url_nested_md(tmp_path, derive_url):
    site = str(tmp_path)
    filepath = os.path.join(site, "legal", "cookies-policy.md")
    assert derive_url(filepath, site) == "https://vyos.net/legal/cookies-policy/"
