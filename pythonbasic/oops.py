class Calculater:
    num = 100 #class variable

    # default condtructor
    
    def __init__(self,a,b):
        self.first = a
        self.second = b
        print("i am called automsticslly when object is created")



    def getdata(self):
        print("my name is naveen")

    def addition(self):
        return self.first + self.second + Calculater.num

    
obj = Calculater(3,4)
obj.getdata()
print(obj.addition())


