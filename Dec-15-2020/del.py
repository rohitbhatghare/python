import shelve
    d = shelve.open("emp.txt")
    d[key] = data
    data = d(key)
    del d[key]
    flag = key in d
    klist(d.keys())
    d['xx'] = [0, 1, 2]
    d['xx'].append(3)
    temp = d['xx']
    temp.append(5)
    d['xx'] = temp
    d.close()