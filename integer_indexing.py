# -*- coding: utf-8 -*- 

import numpy as np
import sys
from pandas import Series, DataFrame

ser = Series(np.arange(3.))
print ser
try:
    print ser[-1] 
except:
    print sys.exc_info()[0]
ser2 = Series(np.arange(3.), index = ['a', 'b', 'c'])
print ser2[-1]
ser3 = Series(range(3), index = [-5, 1, 3])
print ser3.iloc[2]  
print

frame = DataFrame(np.arange(6).reshape((3, 2)), index = [2, 0, 1])
print frame
print frame.iloc[0]
print frame.iloc[:, 1]
