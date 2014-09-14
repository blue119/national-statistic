#!/usr/bin/env python3
#  -*- coding: UTF-8 -*-

from glob import glob

def main():
    """@todo: Docstring for main.
    :returns: @todo

    """
    MATI_META = {}
    CSV_BUCKET_FILES = sorted(glob("tree_list/csv_bucket/*.csv"))

    PRE_CSV_NAME = ""
    for f_csv in CSV_BUCKET_FILES:
        f_csv = f_csv.replace("tree_list/csv_bucket/", "").replace(".csv", "")
        MA, TI, ST, ET = f_csv.split('_')

        MATI_META.setdefault("%s_%s" % (MA, TI), []).append((ST, ET))

    for mati in MATI_META:
        rng = MATI_META[mati]
        new_file = "tree_list/csv_merge/%s_%s_%s.csv" % (mati, rng[0][0], rng[-1][1])
        new_file_p = open(new_file, 'w')
        print(new_file)

        d = rng[0]
        rng_bucket_file = "tree_list/csv_bucket/%s_%s_%s.csv" % (mati, d[0], d[1])
        with open(rng_bucket_file, 'r') as f:
            new_file_p.writelines(f.readlines())

        if len(d) == 1: continue
        for d in rng[1:]:
            rng_bucket_file = "tree_list/csv_bucket/%s_%s_%s.csv" % (mati, d[0], d[1])
            with open(rng_bucket_file, 'r') as f:
                new_file_p.writelines(f.readlines()[1:])

if __name__ == '__main__':
    main()
