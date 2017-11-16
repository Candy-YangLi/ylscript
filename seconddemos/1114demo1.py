#class
class Person:
    def __init__(self,name):
        self.name=name
    def sayhello(self):
        print("my name is %s"%(self.name))
p=Person('yangli223')
p.sayhello()

