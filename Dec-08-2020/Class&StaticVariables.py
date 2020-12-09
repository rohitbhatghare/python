class CSStudent:
    stream = 'cse'
    stream1='ETC'

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


a = CSStudent('Satish', 1)
b = CSStudent('Ranjeet', 2)

print(a.stream)
print(a.name)
print(a.roll)
print(b.stream1)
print(b.name)
print(b.roll)



print(CSStudent.stream)