class Duck:
    def talk(self):
        print('quack..quack..')


class dog:
    def talk(self):
        print('bow bow')


class goat:
    def talk(self):
        print('Myah myah')


def f1(self):
    obj.talk()


l = [Duck(), dog(), goat()]
for obj in l:
    f1(obj)
