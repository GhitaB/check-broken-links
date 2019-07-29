# check-broken-links
Check broken links for a given website

$ mkdir project

$ cd project

$ docker run --rm linkchecker/linkchecker https://foo-website.bar 1 --no-robots > linksintegrity.txt 2>&1
