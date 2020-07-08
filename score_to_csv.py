import sys

if len(sys.argv) == 1:
    print("Needs some file input")
    sys.exit(1)

for name in sys.argv[1:]:
    if name.endswith(".sc") == False:
        continue

    f = None
    try:
        f = open(name, 'r')
    except:
        print("Can't open {}. Make sure it exists".format(name))
        continue
    f.readline()
    data = [i.split()[1:] for i in f.readlines()]
    f.close()
    lines = [','.join(i) for i in data]
    new_name = None
    try:
        new_name = name.split('.')[0] + ".csv"
        f = open(new_name, 'w')
    except:
        print("Couldn't open {}. Make sure it isn't currently open".format(new_name))
        sys.exit(1)
    f.write('\n'.join(lines) + '\n')
    f.close()
