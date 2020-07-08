import argparse 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--i", help  = "list of score files")

args = parser.parse_args() 

file = open(args.i, "r+")

values = []
for line in file: 
	df = pd.read_csv(line.strip())
	top = df.nsmallest(int(.01* len(df.index)),'I_sc')
	animal = line.strip().partition('-')[0]
	values.append([animal, top["I_sc"].mean(), top["I_sc"].std(), top["Irms"].mean(), top["Irms"].std()])

df_values = pd.DataFrame(values, columns = ['Species','I_sc_avg','I_sc_std','Irms_avg', 'Irms_std'])
print(df_values)

def colors_from_values(values, palette_name):
    # normalize the values to range [0, 1]
    normalized = values/10 #(values - min(values)) / (max(values) - min(values))
    # convert to indices
    indices = np.round(normalized * (len(values) - 1)).astype(np.int32)
    # use the indices to get the colors
    palette = sns.color_palette(palette_name, len(values))
    return np.array(palette).take(indices, axis=0)

#fig, (figure)= plt.subplots(nrows=1, figsize=(8,5))
"""
plt.errorbar(df_values['Irms_avg'], df_values['I_sc_avg'],
	xerr = df_values['Irms_std'], yerr = df_values['I_sc_std'], fmt = '.',
	color = 'black', ecolor = 'grey', capsize = 1
	) 
plt.ylim([-40,-20])
plt.xlim([0,6])
#plt.xticks(x)
#plt.title(title)
plt.xlabel("RMSD")
plt.ylabel("Interface Energy")
plt.show()
#plt.savefig("colvar-graphed.png" """
norm  = norm = plt.Normalize(0,10)
sm = plt.cm.ScalarMappable(cmap="YlOrRd", norm=norm)
sm.set_array([])

bar = sns.barplot(x = 'Species', y = 'I_sc_avg', data = df_values, 
	ci = 1.0, errcolor = 'black',
	palette = colors_from_values(df_values['Irms_avg'],"YlOrRd"))
plt.errorbar(x=np.arange(0,len(df_values.index),1),y=df_values['I_sc_avg'],
            yerr=df_values['I_sc_std'], fmt='none', c= 'black', capsize = 2)

bar.invert_yaxis()
cbar = bar.figure.colorbar(sm)
cbar.set_label('RMSD')

bar.set(ylabel = 'Interface Energy', title = 'COV2 - ACE2')
plt.xticks(rotation=90 )
plt.show()


