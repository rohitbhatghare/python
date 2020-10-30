#Write a Python program to check if a given set is superset of itself and superset of another given set
s={20,30,40,50,60}
s1={1,2,3,4,5,6}

print(s.issuperset(s1))
print("For another super set ")
print(s1.issuperset(s))