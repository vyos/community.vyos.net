.PHONY: assets
assets:
	cp -r assets* build/

.PHONY: site
site:
	soupault

all: site assets
