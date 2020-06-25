with open("kolam-moodle.xml", "rt") as fin:
    with open("kolam-shuffled-moodle.xml", "wt") as fout:
        for line in fin:
            fout.write(line.replace('MULTICHOICE:', 'MULTICHOICE_VS:').replace('MULTICHOICE_H:', 'MULTICHOICE_HS:'))

