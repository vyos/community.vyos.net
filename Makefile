.PHONY: site
site:
	soupault ${SOUPAULT_OPTS}

.PHONY: css
css:
	mkdir -p build/
	sass -I sass/ sass/main.sass > build/main.css

all: site css

.PHONY: live
live: css
	soupault --profile live ${SOUPAULT_OPTS}
	python3 scripts/generate-sitemap.py
