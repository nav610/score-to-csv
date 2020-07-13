import pandas as pd 
import os

df = pd.read_csv("score_local_dock.csv") 
ninety_nine_perc = int(.99 * len(df.index))
top = df.nlargest(ninety_nine_perc ,'I_sc')
print(top.head())
print(len(top.index),len(df.index))
top.description.to_csv('delted-pdbs.txt', index = False)

for i in top.description: 
	name = str(i) + ".pdb"
	print(name) 
	os.remove(name)

