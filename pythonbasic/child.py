from oops import Calculater

class Child(Calculater):
    num2 = 200

    def __init__(self):
        Calculater.__init__(self, 0, 0)
        

    def getcompletedata(self):
        return self.num2 + self.num + self.addition

obj = Child()
print(obj.getcompletedata())