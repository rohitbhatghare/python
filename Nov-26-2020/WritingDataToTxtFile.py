f=open("abcd.txt","w")
l=["sunny \n","Bunny \n","Honey \n"]
f.writelines(l)
print("List of lines written to be file succesfully")
f.close()