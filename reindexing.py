# -*- coding: utf-8 -*- 

import numpy as np
from pandas import DataFrame, Series

obj = Series([4.5, 7.2, -5.3, 3.6], index = ['d', 'b', 'a', 'c'])
print obj
obj2 = obj.reindex(['a', 'b', 'd', 'c', 'e'])
print obj2
print obj.reindex(['a', 'b', 'd', 'c', 'e'], fill_value = 0) 
print

obj3 = Series(['blue', 'purple', 'yellow'], index = [0, 2, 4])
print obj3
print obj3.reindex(range(6), method = 'ffill')
print


frame = DataFrame(np.arange(9).reshape(3, 3),
                  index = ['a', 'c', 'd'],
                  columns = ['Ohio', 'Texas', 'California'])
print frame
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
print frame2
print


states = ['Texas', 'Utah', 'California']
print frame.reindex(columns = states)
print


print frame.reindex(index = ['a', 'b', 'c', 'd'],
                    method = 'ffill',
                    columns = states)
print frame.ix[['a', 'b', 'd', 'c'], states]
