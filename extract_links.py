FILENAME_SOURCE = "linksintegrity.txt"
EXCLUDED_KEYWORDS = ["threads active", "Check time", "Size", "WARNING"]
FILENAME_OUTPUT = "links-output.txt"

with open(FILENAME_SOURCE) as f:
    content = f.readlines()

# content = [x.strip() for x in content]


def ok_line(line):
    for keyword in EXCLUDED_KEYWORDS:
        if keyword in line:
            return False
    return True


with open(FILENAME_OUTPUT, 'a') as g:
    for line in content:
        if ok_line(line):
            g.write(line)
