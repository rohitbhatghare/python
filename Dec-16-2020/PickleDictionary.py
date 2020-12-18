import pickle

f1 = open("datafile.txt", "rb")
emp = pickle.load(f1)
print(emp)