import pickle
f1 = open("EmpID.pickle", 'rb')
emp = pickle.load(f1)
print(emp)