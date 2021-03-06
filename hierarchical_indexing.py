data = Series(np.random.randn(10),
              index = [['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                       [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print data
print data.index
print data.b
print data['b':'c']
print data[:2]
print data.unstack()
print data.unstack().stack()
print

frame = DataFrame(np.arange(12).reshape((4, 3)),
                  index = [['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns = [['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']])
print frame
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
print frame
print frame.ix['a', 1]
print frame.ix['a', 2]['Colorado']
print frame.ix['a', 2]['Ohio']['Red']
print

print MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Gree', 'Red', 'Green']],
                             names = ['state', 'color'])
