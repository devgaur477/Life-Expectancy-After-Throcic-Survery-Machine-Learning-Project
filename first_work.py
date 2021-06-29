# Kernel SVM

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
pd.options.mode.chained_assignment = None  # default='warn'
# Importing the dataset
dataset = pd.read_csv('ThoraricSurgery.csv')






dataset.PRE32[dataset.PRE32 == 'T'] = 1
dataset.PRE32[dataset.PRE32 == 'F'] = 0
dataset.PRE30[dataset.PRE30 == 'T'] = 1
dataset.PRE30[dataset.PRE30 == 'F'] = 0
dataset.PRE25[dataset.PRE25 == 'T'] = 1
dataset.PRE25[dataset.PRE25 == 'F'] = 0
dataset.PRE19[dataset.PRE19 == 'T'] = 1
dataset.PRE19[dataset.PRE19 == 'F'] = 0
dataset.PRE17[dataset.PRE17 == 'T'] = 1
dataset.PRE17[dataset.PRE17 == 'F'] = 0
dataset.PRE14[dataset.PRE14 == 'OC11'] = -1
dataset.PRE14[dataset.PRE14 == 'OC12'] = -2
dataset.PRE14[dataset.PRE14 == 'OC13'] = -3
dataset.PRE14[dataset.PRE14 == 'OC14'] = -4
dataset.PRE11[dataset.PRE11 == 'T'] = 1
dataset.PRE11[dataset.PRE11 == 'F'] = 0
dataset.PRE10[dataset.PRE10 == 'T'] = 1
dataset.PRE10[dataset.PRE10 == 'F'] = 0
dataset.PRE9[dataset.PRE9 == 'T'] = 1
dataset.PRE9[dataset.PRE9 == 'F'] = 0
dataset.PRE8[dataset.PRE8 == 'T'] = 1
dataset.PRE8[dataset.PRE8 == 'F'] = 0
dataset.PRE7[dataset.PRE7 == 'T'] = 1
dataset.PRE7[dataset.PRE7 == 'F'] = 0
dataset.Risk1Yr[dataset.Risk1Yr == 'T'] = 1
dataset.Risk1Yr[dataset.Risk1Yr == 'F'] = 0
dataset.PRE6[dataset.PRE6 == 'PRZ0'] = 0
dataset.PRE6[dataset.PRE6 == 'PRZ1'] = -1
dataset.PRE6[dataset.PRE6 == 'PRZ2'] = -2





x = dataset.iloc[ :, 3:-1].values
y = dataset.iloc[:, -1].values



print(x)

#PRZ is a scale where 0 is the best and 5 is the worst in this dataset we just have till 2 that is 

# PRZ0 non restricted and fully active , PRZ1 able to carry out light work , PRZ2 resting 50% of the day




dataset.to_csv('final_data2.csv')




'''
for i in range(0 , 20):
    if(x[i].all() == 'T'):
        z.append('1')
    else:
        z.append('0')
print(z)
    
'''
'''
for j in range(0,20):
    if x[j].all() == 'OC11':
        w.append('1')
    if x[j].all() == 'OC12':
        w.append('2')
    if x[j].all() == 'OC13':
        w.append('3')
    if x[j].all() == 'OC14':
        w.append('4')


print(w)
# for size of tumour levels , 1 is the smallest and 4 is the largest

'''

