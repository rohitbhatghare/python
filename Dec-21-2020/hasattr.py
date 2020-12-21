class Duck:
    def talk(self):
        print('quack.quak')


class dog:
    def bark(self):
        print('bow bow')


class goat:
    def talk(self):
        print('Myah myah..')


def f1(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()

d=Duck()
f1(d)

g=goat
f1(d)
d=dog()
f1(d)
