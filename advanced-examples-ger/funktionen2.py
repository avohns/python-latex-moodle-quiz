with open("funktionen-moodle.xml", "rt") as fin:
    with open("funktionen-shuffled-moodle.xml", "wt") as fout:
        for line in fin:
            fout.write(line.replace('MULTICHOICE:', 'MULTICHOICE_S:'))

