#!/usr/bin/env python3
#
# Builds a list of nightly builds from S3
#
# Requires the following environment variables:
# SNAPSHOTS_BUCKET
# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY

import os
import re
import json

import boto3

import jinja2

from functools import cmp_to_key

bucket = os.getenv("SNAPSHOTS_BUCKET")

def make_link(s, f):
    f = re.sub(r'\s+', '+', f)
    return "https://s3.amazonaws.com/{0}/rolling/current/{1}".format(bucket, f)

def compare(l, r):
    try:
        regex = r'\-(\d+)\-'
        l_date = int(re.search(regex, l).group(1))
        r_date = int(re.search(regex, r).group(1))
        if l_date == r_date:
            return 0
        elif l_date > r_date:
            return 1
        else:
            return -1
    except:
        return(-1)


s3 = boto3.client('s3')
object_listing = s3.list_objects_v2(Bucket=bucket, Prefix='rolling/current')
data = object_listing['Contents']

files = []
for f in data:
    files.append(f['Key'])

file_names = list(set(map(lambda s: re.sub(r'rolling/current/(.*?)', r'\1', s), files)))
file_names.sort(reverse=True, key=cmp_to_key(compare))

builds = []

for name in file_names:
    build = {}
    build['file'] = name
    build['link'] = make_link('rolling', name)

    builds.append(build)

tmpl = jinja2.Template("""
<ul>
{% for b in builds %}
  <li><a href="{{b.link}}">{{b.file}}</a></li>
{% endfor %}
</ul>
""")
