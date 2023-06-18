# Consider a superclass PurchaseItem which models customer’s purchases. This class has:
# - two variables name (String) and unitPrice (double).
# - One constructor to initialize the instance variables.
# - A default constructor to initialize name to “no item”, and unitPrice to 0
# - A method getPrice that returns the unitPrice.
# Consider two subclasses WeighedItem and CountedItem. WeighedItem has an additional instance
# variable weight (double) in Kg while CountedItem has an additional variable quantity (int).
# - Write an appropriate constructor for each of the classes making use of the constructor of the
# superclass to initialize its members.
# - getPrice method that returns the price of the purchasedItem based on its unit price and weight
# (WeighedItem), or quantity (CountedItem). Make use of getPrice of the superclass.
# Write an application class where you construct objects from the two subclasses and print them on
# the screen.

class PurchaseItem :
    def __init__(self,name='no item',unitPrice=0,quantity=0) :
        self.name=name
        self.unitPrice=unitPrice
        self.quantity=quantity
    
    def getPrice(self) :
        return self.unitPrice*self.quantity
    
class WeighedItem(PurchaseItem) :
    def __init__(self,name,unitPrice,weight) :
        super().__init__(name,unitPrice,weight)

class CountedItem(PurchaseItem) :
    def __init__(self,name,unitPrice,counts) :
        super().__init__(name,unitPrice,counts)

class application(WeighedItem,CountedItem) :
    
    def __init__(self) :
        self.name=input('Enter the item name :')
        self.price=int(input('Enter the unit Price :'))
        self.type=input('Do you have counts or weight :')
        
    def purchase(self) :
        if self.type=='counts' :
            quantity=int(input('Enter the counts :'))
            WeighedItem.__init__(self,self.name,self.price,quantity)
            return self.getPrice()
        elif self.type=='weight' :
            quantity=int(input('Enter the weight :'))
            CountedItem.__init__(self,self.name,self.price,quantity)     
            return self.getPrice()

p=application()
print('Rs.',p.purchase())