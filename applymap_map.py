# -*- coding: utf-8 -*- 

import numpy as np
from pandas import Series, DataFrame

frame = DataFrame(np.random.randn(4, 3),
                  columns = list('bde'),
                  index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
print frame
print np.abs(frame)
print

f = lambda x: x.max() - x.min()
print frame.apply(f)
print frame.apply(f, axis = 1)
def f(x):
    return Series([x.min(), x.max()], index = ['min', 'max'])
print frame.apply(f)
print

print 'applymap and map'
_format = lambda x: '%.2f' % x
print frame.applymap(_format)
print frame['e'].map(_format)
