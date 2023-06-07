# Create a class called ITEMS which should have all the item names with its code. Create another class
# called DETAILS which contains the methods getPrice(int code) and getName(int code) to return the
# price and name of a particular item code. Create a class SHOP that inherits the classes ITEMS and
# DETAILS. Define the main method that should ask the user to enter the item code and display the
# product name and price based on the item code.

class DETAILS :
    def __init__(self) :
        self.lst={100:['Pencil',10],101:['InkPen',25],102:['Eraser',5],103:['Scale',15],104:['BluePen',12],105:['BlackPen',12],106:['Note',50],107:['Sharpener',8]}
    
    def getname(self,code) :
        if code in self.lst.keys() :
            return self.lst[code][0]
        else : 
            return -1
    
    def getprice(self,code) :
        if code in self.lst.keys() :
            return self.lst[code][1]
        else :
            return -1

class SHOP(DETAILS) : 
    def __init__(self) :
        self.code=-1
        super().__init__()
        self.name=''
        self.price=0

    def product(self) :
        self.code=int(input('Enter the code of the item :'))
        self.name=self.getname(self.code)
        self.price=self.getprice(self.code)
        
person1=SHOP()
person1.product()
print('Item name :',person1.name)
print('Item price :Rs.',person1.price)