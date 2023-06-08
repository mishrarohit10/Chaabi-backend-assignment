from functools import reduce

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
#output = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
A1 = range(10)
#output = range(0, 10)
A2 = sorted([i for i in A1 if i in A0])
#output = []
A3 = sorted([A0[s] for s in A0])
#output = [1, 2, 3, 4, 5]
A4 = [i for i in A1 if i in A3]
#output = [1, 2, 3, 4, 5]
A5 = {i:i*i for i in A1}
#output = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
A6 = [[i,i*i] for i in A1]
#output = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
#output = 21
A8 = map(lambda x: x*2, [1,2,3,4])
#output = <map object at 0x000001DA7689B310>
A9 = filter(lambda x: len(x)>3,["I","want","to","learn","python"])
#output = <filter object at 0x0000023573B9B1F0>