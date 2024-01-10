import os
import glob

base_dir = os.path.join(os.path.dirname(os.getcwd()), 'data')
in_dir = os.path.join(base_dir, 'publications')
out_file = os.path.join(base_dir, 'publications.yml')

out_f = open(out_file, 'w')
out_f.write("years:\n")

years = os.listdir(in_dir)
years.sort(reverse=True)

for year in years:
    out_f.write("  - year: {}\n".format(year))
    out_f.write("    papers:\n")
    yml_files = glob.glob(os.path.join(in_dir, year, '*.yml'))
    yml_files.sort(reverse=True)

    for yml_file in yml_files:
        basename = os.path.splitext(os.path.basename(yml_file))[0]
        print(basename)
        out_f.write("      - name: {}\n".format(basename))
        with open(yml_file) as in_f:
            lines = in_f.readlines()
            for line in lines:
                out_f.write("        {}".format(line))
