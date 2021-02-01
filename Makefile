.PHONY: site
site:
	soupault ${SOUPAULT_OPTS}

.PHONY: css
css:
	mkdir -p build/
	sass -I sass/ sass/main.sass > build/main.css

all: site css
