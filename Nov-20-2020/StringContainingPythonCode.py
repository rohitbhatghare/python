code = 'print("hello world")'
mycode = """
def mutiply(x,y):
    return x*y

print('Multiply of 2 and 3 is: ',mutiply(2,3))
"""
exec(code)
exec(mycode)