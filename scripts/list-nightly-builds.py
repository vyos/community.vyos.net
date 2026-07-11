#!/usr/bin/env python3
#
# Builds a list of nightly builds from GitHub releases
#
# Requires the following environment variables:
# SNAPSHOTS_BUCKET
# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY

import os
import re
import sys
import json

import github
import jinja2

REPO = 'vyos/vyos-nightly-build'

def list_images(repo):
    images = []

    # GitHub returns releases sorted by date from newest to oldest,
    # so we don't need to sort them
    releases = repo.get_releases()
    for r in releases:
        # Match assets by filename instead of by position: each release has
        # exactly one ISO plus its Minisign signature (<iso-name>.minisig),
        # alongside other assets (checksums, source archives, etc.) whose
        # count varies over time. Index-based access breaks whenever that
        # count changes, so look the pair up by name.
        assets = {a.name: a for a in r.assets}

        iso = next((a for name, a in assets.items() if name.endswith(".iso")), None)
        if iso is None:
            continue  # no ISO in this release, skip

        sig = assets.get(iso.name + ".minisig")
        if sig is None:
            continue  # ISO without a signature, skip

        image = {}
        image["iso_url"] = iso.browser_download_url
        image["sig_url"] = sig.browser_download_url
        image["title"] = r.name  # r.title is deprecated in PyGithub

        images.append(image)

    return images

def render_image_list(images):
    tmpl = jinja2.Template("""
      <ul>
      {% for i in images %}
        <li><a href="{{i.iso_url}}">{{i.title}}</a> (<a href="{{i.sig_url}}">sig</a>)</li>
      {% endfor %}
     </ul>
    """)

    return tmpl.render(images=images)

if __name__ == '__main__':
    gh_token_string = os.getenv('GH_ACCESS_TOKEN')
    gh_auth = github.Auth.Token(gh_token_string)
    gh = github.Github(auth=gh_auth)
    repo = gh.get_repo(REPO)

    images = list_images(repo)
    print(render_image_list(images))