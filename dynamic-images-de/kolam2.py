with open("kolam-moodle.xml", "rt") as fin:
    with open("kolam-shuffled-moodle.xml", "wt") as fout:
        for line in fin:
            fout.write(line.replace('{multi}CHOICE:', '{multi}CHOICE_VS:').replace('{multi}CHOICE_H:', '{multi}CHOICE_HS:'))

