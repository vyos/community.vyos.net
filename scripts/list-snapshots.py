#!/usr/bin/env python3

# Requires the following environment variables:
# SNAPSHOTS_BUCKET
# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY

import os
import re
import json

import boto3

import jinja2

bucket = os.getenv("SNAPSHOTS_BUCKET")

def make_link(s, f):
    f = re.sub(r'\s+', '+', f)
    return "https://s3.amazonaws.com/{0}/{1}".format(bucket, f)

s3 = boto3.client('s3')
object_listing = s3.list_objects_v2(Bucket=bucket, Prefix='snapshot')
data = object_listing['Contents']

files = []
for f in data:
    files.append(f['Key'])

snapshot_names = set(map(lambda s: re.sub(r'snapshot/(.*?)/.*', r'\1', s), files))

snapshots = []


for name in snapshot_names:
    snapshot = {}
    snapshot['name'] = name
    snapshot['files'] = list(filter(lambda s: re.search(name, s), files))

    snapshot_files = list(filter(lambda s: re.search(name, s), files))
    snapshot_files = list(map(lambda f: {'name': os.path.basename(f).strip(), 'platform': os.path.basename(os.path.dirname(f)), 'link': make_link(name, f)}, snapshot_files))

    # S3 listing sometimes returns dir names among file names... filter those out.
    snapshot_files = list(filter(lambda f: f['name'] != "", snapshot_files))

    snapshot['files'] = snapshot_files

    snapshots.append(snapshot)

tmpl = jinja2.Template("""
{% for s in snapshots %}
  <h3>{{s.name}}</h3>
  <ul>
  {% for f in s.files %}
    <li><a href="{{f.link}}">{{f.name}} ({{f.platform}})</a></li>
  {% endfor %}
  </ul>
{% endfor %}
""")

print(tmpl.render(snapshots=snapshots))
