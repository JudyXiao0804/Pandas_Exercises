# -*- coding: utf-8 -*- 

import numpy as np
from pandas import DataFrame

frame = DataFrame({'a':range(7),
                   'b':range(7, 0, -1),
                   'c':['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                   'd':[0, 1, 2, 0, 1, 2, 3]})
print frame
print frame.set_index(['c', 'd']) 
print frame.set_index(['c', 'd'], drop = False) 
frame2 = frame.set_index(['c', 'd'])
print frame2.reset_index()

