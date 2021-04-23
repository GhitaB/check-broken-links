# check-broken-links
Check broken links for a given website

$ git clone git@github.com:GhitaB/check-broken-links.git

$ cd check-broken-links

$ docker run --rm linkchecker/linkchecker https://foo-website.bar 1 --no-robots > linksintegrity.txt 2>&1

Wait...

$ python extract_links.py

Open links-output.txt.

[![Contact me on Codementor](https://www.codementor.io/m-badges/ghitab/find-me-on-cm-b.svg)](https://www.codementor.io/@ghitab?refer=badge)
