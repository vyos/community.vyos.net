# community.vyos.net

The VyOS community website.

## Repository structure

```
templates/		Page skeletons and chunks of reusable HTML.
templates/main.html	An empty page skeleton.

site/			Site pages.

scripts/		Helper scripts.

soupault.conf		Configuration file for the soupault static site generator.
```

## Branches

This repository has two branches: `main` and `production`.

The `main` branch serves as a staging environment where all new changes to first.
It's automatically deployed to the staging.vyos.net domain so that the changes
can be viewed live.

The `production` branch is deployed to the real [vyos.net] website.

## Contributing

The fundamental structure of the website is not set in stone yet, so if you want to add a new page
or rearrange any directories and pages, ask the maintainers first!

Typo/grammar fixes, fixes for broken links or formatting, and other changes that fix a specific problem
are more than welcome!

## Building

We encourage you to make sure that the site builds and looks as expected before making a pull request.

Two tools are _required_ for building:

* [soupault](https://soupault.app) static site generator.
* [SASS](https://sass-lang.com/) compiler, the Dart version.

**Note:** the C++ `sassc` _will not_ work! The Dart and the C++ "reference implementations" don't behave the same,
and you'll need the Dart one (available from NPM, `npm install -g sass`).
Hopefully we'll rid this site of SASS some day and it will be no longer an issue.

Running `make all` will build both the site and the CSS, generated files will be in `build/`.
You can then preview the site with any development web server, e.g. `python3 -m http.server --directory build/`.

### snapshot and nightly build pages

If you build the website as described, your `/get/snapshots` and `/get/nightly-builds` pages will not actually list any builds.
This is normal. Those image lists are generated from an S3 bucket contents by `scripts/list-snapshots.py`
and `scripts/list-nightly-builds.py`. Their output is inserted into pages at build time,
see `[widgets.list-snapshots]` and `[widgets.list-nightly-builds]` sections in `soupault.conf` for details.

They are disabled by default, limited to the soupault profile `live`.

You can force soupault to run them by building with `soupault --profile live`. You'll need an appropriate
S3 bucket that mimics our own setup and access credentials for it in your environment.
All in all you probably don't want to touch them since they are really specific to our own setup.
This section is here mostly for completeness.
