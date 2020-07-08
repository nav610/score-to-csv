import sys

if len(sys.argv) != 3:
    print("Needs two inputs. File to extract from, and file with names")
    sys.exit(1)

f_input = open(sys.argv[1], 'r')
header = f_input.readline()
lines = [i.split(',') for i in f_input.readlines()]
processed_lines = {i[32].strip():i for i in lines}
f_input.close()

f_read = open(sys.argv[2], 'r')
f_out = open(sys.argv[2].split('.')[0]+'.csv', 'w')

f_out.write(header)
for i in f_read.readlines():
    f_out.write(','.join(processed_lines[i.split('.')[0]]))

f_out.close()
f_read.close()
