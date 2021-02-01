.PHONY: site
site:
	soupault ${SOUPAULT_OPTS}

.PHONY: css
css:
	sass -I sass/ sass/main.sass > build/css/main.css

all: site css
