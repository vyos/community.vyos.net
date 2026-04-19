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
