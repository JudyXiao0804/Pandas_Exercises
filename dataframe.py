# -*- coding: utf-8 -*- 

import numpy as np
from pandas import Series, DataFrame

data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year':[2000, 2001, 2002, 2001, 2002],
        'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}
print DataFrame(data)
print DataFrame(data, columns = ['year', 'state', 'pop'])
print

frame2 = DataFrame(data,
                    columns = ['year', 'state', 'pop', 'debt'],
                    index = ['one', 'two', 'three', 'four', 'five'])
print frame2
print frame2['state']
print frame2.year
print frame2.ix['three']
frame2['debt'] = 16.5 
print frame2
frame2.debt = np.arange(5)  
print frame2
print

val = Series([-1.2, -1.5, -1.7], index = ['two', 'four', 'five'])
frame2['debt'] = val
print frame2
print

frame2['eastern'] = (frame2.state == 'Ohio') 
print frame2
print frame2.columns
print


pop = {'Nevada':{2001:2.4, 2002:2.9},
        'Ohio':{2000:1.5, 2001:1.7, 2002:3.6}}
frame3 = DataFrame(pop)
print frame3
print frame3.T
print


print DataFrame(pop, index = [2001, 2002, 2003])
pdata = {'Ohio':frame3['Ohio'][:-1], 'Nevada':frame3['Nevada'][:2]}
print DataFrame(pdata)
print


frame3.index.name = 'year'
frame3.columns.name = 'state'
print frame3
print frame3.values
print frame2.values
