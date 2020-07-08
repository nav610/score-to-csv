import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("-i","--i",help="file with dock scores")

args = parser.parse_args()
df=pd.read_csv(args.i)
row =df.loc[df['I_sc'].idxmin()]

f=open("lowest_docked_pdb.txt", "a+")
f.write(str(row['I_sc']) + "  ")
f.write(str(row['Irms']) + "  ")
f.write(str(row['description']))
f.write("\n")
f.close()
print(row['I_sc'],row['Irms'],row['description'])
