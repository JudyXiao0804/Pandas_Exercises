# -*- coding: utf-8 -*- 

import numpy as np
from numpy import nan as NA
import pandas as pd
from pandas import Series, DataFrame, Index

df = DataFrame(np.random.randn(7, 3))
df.ix[:4, 1] = NA
df.ix[:2, 2] = NA
print df.fillna(0)
df.fillna(0, inplace = True)
print df
print

print df.fillna({1:0.5, 3:-1}) 
print

df = DataFrame(np.random.randn(6, 3))
df.ix[2:, 1] = NA
df.ix[4:, 2] = NA
print df
print df.fillna(method = 'ffill')
print df.fillna(method = 'ffill', limit = 2)
print

data = Series([1., NA, 3.5, NA, 7])
print data.fillna(data.mean())
