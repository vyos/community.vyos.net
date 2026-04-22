import os
import xml.etree.ElementTree as ET
import pytest

NS = "http://www.sitemaps.org/schemas/sitemap/0.9"


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


def test_get_heuristics_root(get_heuristics):
    changefreq, priority = get_heuristics("/")
    assert changefreq == "daily"
    assert priority == "1.0"


def test_get_heuristics_depth1(get_heuristics):
    changefreq, priority = get_heuristics("/about/")
    assert changefreq == "weekly"
    assert priority == "0.8"


def test_get_heuristics_depth2_default(get_heuristics):
    changefreq, priority = get_heuristics("/legal/cookies-policy/")
    assert changefreq == "monthly"
    assert priority == "0.5"


def test_get_heuristics_get_override(get_heuristics):
    changefreq, priority = get_heuristics("/get/")
    assert changefreq == "daily"
    assert priority == "0.8"


def test_get_heuristics_nightly_builds_override(get_heuristics):
    changefreq, priority = get_heuristics("/get/nightly-builds/")
    assert changefreq == "daily"
    assert priority == "0.5"


def test_get_heuristics_depth3_uses_depth2_default(get_heuristics):
    changefreq, priority = get_heuristics("/a/b/c/")
    assert changefreq == "monthly"
    assert priority == "0.5"


def make_full_site(tmp_path):
    """Create a site/ tree matching the current vyos.net structure."""
    files = [
        "index.html",
        "about/index.md",
        "about/upstream-projects.md",
        "contribute/index.md",
        "get/index.md",
        "get/contributor-subscriptions.md",
        "get/nightly-builds.md",
        "get/stream.md",
        "status.md",
        "legal/cookies-policy.md",
        "img/logo.svg",
        "js/app.js",
    ]
    return make_site(tmp_path / "site", files)


def test_generate_sitemap_produces_xml(tmp_path, generate_sitemap):
    site = make_full_site(tmp_path)
    build = tmp_path / "build"
    build.mkdir()
    generate_sitemap(str(site), str(build), today="2026-04-19")
    out = build / "sitemap.xml"
    assert out.exists()


def test_generate_sitemap_well_formed(tmp_path, generate_sitemap):
    site = make_full_site(tmp_path)
    build = tmp_path / "build"
    build.mkdir()
    generate_sitemap(str(site), str(build), today="2026-04-19")
    ET.parse(str(build / "sitemap.xml"))  # raises if not well-formed


def test_generate_sitemap_namespace(tmp_path, generate_sitemap):
    site = make_full_site(tmp_path)
    build = tmp_path / "build"
    build.mkdir()
    generate_sitemap(str(site), str(build), today="2026-04-19")
    tree = ET.parse(str(build / "sitemap.xml"))
    root = tree.getroot()
    assert root.tag == f"{{{NS}}}urlset"


def test_generate_sitemap_url_count(tmp_path, generate_sitemap):
    site = make_full_site(tmp_path)
    build = tmp_path / "build"
    build.mkdir()
    generate_sitemap(str(site), str(build), today="2026-04-19")
    tree = ET.parse(str(build / "sitemap.xml"))
    root = tree.getroot()
    urls = root.findall(f"{{{NS}}}url")
    assert len(urls) == 10


def test_generate_sitemap_all_fields_present(tmp_path, generate_sitemap):
    site = make_full_site(tmp_path)
    build = tmp_path / "build"
    build.mkdir()
    generate_sitemap(str(site), str(build), today="2026-04-19")
    tree = ET.parse(str(build / "sitemap.xml"))
    root = tree.getroot()
    for url_el in root.findall(f"{{{NS}}}url"):
        assert url_el.find(f"{{{NS}}}loc") is not None
        assert url_el.find(f"{{{NS}}}lastmod") is not None
        assert url_el.find(f"{{{NS}}}changefreq") is not None
        assert url_el.find(f"{{{NS}}}priority") is not None


def test_generate_sitemap_lastmod_is_today(tmp_path, generate_sitemap):
    site = make_full_site(tmp_path)
    build = tmp_path / "build"
    build.mkdir()
    generate_sitemap(str(site), str(build), today="2026-04-19")
    tree = ET.parse(str(build / "sitemap.xml"))
    root = tree.getroot()
    for url_el in root.findall(f"{{{NS}}}url"):
        assert url_el.find(f"{{{NS}}}lastmod").text == "2026-04-19"


def test_generate_sitemap_urls_sorted(tmp_path, generate_sitemap):
    site = make_full_site(tmp_path)
    build = tmp_path / "build"
    build.mkdir()
    generate_sitemap(str(site), str(build), today="2026-04-19")
    tree = ET.parse(str(build / "sitemap.xml"))
    root = tree.getroot()
    locs = [el.find(f"{{{NS}}}loc").text for el in root.findall(f"{{{NS}}}url")]
    assert locs == sorted(locs)


def test_generate_sitemap_no_duplicate_locs(tmp_path, generate_sitemap):
    site = make_full_site(tmp_path)
    build = tmp_path / "build"
    build.mkdir()
    generate_sitemap(str(site), str(build), today="2026-04-19")
    tree = ET.parse(str(build / "sitemap.xml"))
    root = tree.getroot()
    locs = [el.find(f"{{{NS}}}loc").text for el in root.findall(f"{{{NS}}}url")]
    assert len(locs) == len(set(locs))


def test_generate_sitemap_root_heuristics(tmp_path, generate_sitemap):
    site = make_full_site(tmp_path)
    build = tmp_path / "build"
    build.mkdir()
    generate_sitemap(str(site), str(build), today="2026-04-19")
    tree = ET.parse(str(build / "sitemap.xml"))
    root = tree.getroot()
    root_url = next(
        el for el in root.findall(f"{{{NS}}}url")
        if el.find(f"{{{NS}}}loc").text == "https://vyos.net/"
    )
    assert root_url.find(f"{{{NS}}}priority").text == "1.0"
    assert root_url.find(f"{{{NS}}}changefreq").text == "daily"


def test_generate_sitemap_get_override(tmp_path, generate_sitemap):
    site = make_full_site(tmp_path)
    build = tmp_path / "build"
    build.mkdir()
    generate_sitemap(str(site), str(build), today="2026-04-19")
    tree = ET.parse(str(build / "sitemap.xml"))
    root = tree.getroot()
    get_url = next(
        el for el in root.findall(f"{{{NS}}}url")
        if el.find(f"{{{NS}}}loc").text == "https://vyos.net/get/"
    )
    assert get_url.find(f"{{{NS}}}changefreq").text == "daily"


def test_generate_sitemap_nightly_builds_override(tmp_path, generate_sitemap):
    site = make_full_site(tmp_path)
    build = tmp_path / "build"
    build.mkdir()
    generate_sitemap(str(site), str(build), today="2026-04-19")
    tree = ET.parse(str(build / "sitemap.xml"))
    root = tree.getroot()
    nb_url = next(
        el for el in root.findall(f"{{{NS}}}url")
        if el.find(f"{{{NS}}}loc").text == "https://vyos.net/get/nightly-builds/"
    )
    assert nb_url.find(f"{{{NS}}}changefreq").text == "daily"


def test_generate_sitemap_error_on_missing_site(tmp_path, generate_sitemap):
    build = tmp_path / "build"
    build.mkdir()
    with pytest.raises(SystemExit) as exc:
        generate_sitemap(str(tmp_path / "nonexistent"), str(build), today="2026-04-19")
    assert exc.value.code == 1


def test_generate_sitemap_error_on_zero_pages(tmp_path, generate_sitemap):
    site = tmp_path / "site"
    site.mkdir()
    build = tmp_path / "build"
    build.mkdir()
    with pytest.raises(SystemExit) as exc:
        generate_sitemap(str(site), str(build), today="2026-04-19")
    assert exc.value.code == 1


def test_generate_sitemap_error_on_duplicate_urls(tmp_path, generate_sitemap):
    # foo.md and foo.html at the same path both derive to /foo/
    site = make_site(tmp_path / "site", ["foo.md", "foo.html"])
    build = tmp_path / "build"
    build.mkdir()
    with pytest.raises(SystemExit) as exc:
        generate_sitemap(str(site), str(build), today="2026-04-19")
    assert exc.value.code == 1
