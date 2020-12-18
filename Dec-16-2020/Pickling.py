import pickle
EmpID = {1:"Nish",2:"Rohit",3:"Abhilash",4:"Amit",5:"Tejas"}
f1 = open("EmpID.pickle","wb")
pickle.dump(EmpID, f1)
f1.close()
print("File Written Successful")