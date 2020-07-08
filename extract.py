import argparse, sys
sc_available = None
try:
    from spellchecker import SpellChecker
    sc_available = True
except:
    sc_available = False

parser = argparse.ArgumentParser(description="Extract specific columns from a csv file")
parser.add_argument("file", type=argparse.FileType('r'), help="File to extract from")
parser.add_argument("field", type=str, nargs='+', help="Field(s) to extract")
parser.add_argument("--tab", action="store_true", help="Outputs results as tab separated instead of comma separated")
parser.add_argument("--no_names", action="store_true", help="Prevents outputing header names")

args = parser.parse_args()

lines = args.file.readlines()

keywords = {name:n for (n,name) in enumerate(lines[0].split(','))}

nums = []
for field in args.field:
    try:
        nums.append(keywords[field])
    except:
        if sc_available:
            sc = SpellChecker(language=None, case_sensitive=True)
            sc.word_frequency.load_words(keywords.keys())

            print("{} not found. Did you mean {}? Quitting".format(field, sc.correction(field)))
        else:
            print("{} not found. Install pyspellchecker to get suggestions. Quitting".format(field))
        sys.exit(1)

sep = None
if args.tab:
    sep = '\t'
else:
    sep = ','

start = None
if args.no_names:
    start = 1
else:
    start = 0

for line in lines[start:]:
    line = line.split(',')
    print(sep.join([line[i] for i in nums]))
