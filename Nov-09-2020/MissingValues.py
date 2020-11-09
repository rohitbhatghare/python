l1 = ['a','b','c','d','e','f']
l2 = ['d','e','f','g','h']
print('Missing values in second list: ', ','.join(set(l1).difference(l2)))
print('Additional values in second list: ', ','.join(set(l2).difference(l1)))