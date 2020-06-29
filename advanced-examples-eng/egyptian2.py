with open("egyptian-moodle.xml", "rt") as fin:
    with open("egyptian-moodle-ready.xml", "wt") as fout:
        for line in fin:
            fout.write(line.replace('&rdquo;', '\"').replace('&rsquo;', '\''))

