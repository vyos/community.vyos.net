#!/usr/bin/env python3
import os
import sys
import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom

BASE_URL = "https://vyos.net"

ASSET_DIRS = {"img", "js", "favicon"}

OVERRIDES = {
    "/get/": {"changefreq": "daily", "priority": "0.8"},
    "/get/nightly-builds/": {"changefreq": "daily", "priority": "0.5"},
}

DEPTH_DEFAULTS = [
    {"changefreq": "daily",   "priority": "1.0"},   # depth 0
    {"changefreq": "weekly",  "priority": "0.8"},   # depth 1
    {"changefreq": "monthly", "priority": "0.5"},   # depth 2+
]


def find_pages(site_dir):
    """Return list of absolute paths to routable page source files."""
    pages = []
    for dirpath, dirnames, filenames in os.walk(site_dir):
        dirnames[:] = [d for d in dirnames if d not in ASSET_DIRS]
        for fname in filenames:
            if fname.endswith((".md", ".html")):
                pages.append(os.path.join(dirpath, fname))
    return pages


def derive_url(filepath, site_dir):
    """Derive canonical URL from a source file path relative to site_dir."""
    rel = os.path.relpath(filepath, site_dir)
    parts = rel.replace(os.sep, "/").split("/")
    stem = os.path.splitext(parts[-1])[0]
    if stem == "index":
        path_parts = parts[:-1]
    else:
        path_parts = parts[:-1] + [stem]
    if not path_parts:
        url_path = "/"
    else:
        url_path = "/" + "/".join(path_parts) + "/"
    return BASE_URL + url_path


def get_heuristics(url_path):
    """Return (changefreq, priority) tuple for a URL path string."""
    if url_path in OVERRIDES:
        o = OVERRIDES[url_path]
        return o["changefreq"], o["priority"]
    depth = len([s for s in url_path.split("/") if s])
    idx = min(depth, 2)
    d = DEPTH_DEFAULTS[idx]
    return d["changefreq"], d["priority"]


def generate_sitemap(site_dir, build_dir, today=None):
    """Discover pages in site_dir and write build_dir/sitemap.xml."""
    if today is None:
        today = datetime.date.today().isoformat()

    if not os.path.isdir(site_dir):
        print(f"Error: site directory not found: {site_dir}", file=sys.stderr)
        sys.exit(1)

    pages = find_pages(site_dir)
    if not pages:
        print("Error: no routable pages discovered in site/", file=sys.stderr)
        sys.exit(1)

    # Derive URLs, detect duplicates
    url_to_source = {}
    for page in pages:
        url = derive_url(page, site_dir)
        if url in url_to_source:
            print(
                f"Error: duplicate URL {url} from:\n"
                f"  {url_to_source[url]}\n"
                f"  {page}",
                file=sys.stderr,
            )
            sys.exit(1)
        url_to_source[url] = page

    # Build XML tree
    urlset = ET.Element("urlset")
    urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")

    for url in sorted(url_to_source):
        url_path = url[len(BASE_URL):]
        changefreq, priority = get_heuristics(url_path)
        url_el = ET.SubElement(urlset, "url")
        ET.SubElement(url_el, "loc").text = url
        ET.SubElement(url_el, "lastmod").text = today
        ET.SubElement(url_el, "changefreq").text = changefreq
        ET.SubElement(url_el, "priority").text = priority

    # Pretty-print via minidom
    raw = ET.tostring(urlset, encoding="unicode")
    dom = minidom.parseString(raw)
    pretty = dom.toprettyxml(indent="  ", encoding="UTF-8")

    out_path = os.path.join(build_dir, "sitemap.xml")
    with open(out_path, "wb") as f:
        f.write(pretty)
    print(f"Wrote {out_path}")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    site_dir = os.path.join(repo_root, "site")
    build_dir = os.path.join(repo_root, "build")
    generate_sitemap(site_dir, build_dir)


if __name__ == "__main__":
    main()
