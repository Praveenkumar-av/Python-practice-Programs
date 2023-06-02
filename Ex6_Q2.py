# Write a class called Product. The class should have fields called name, amount, 
# and price, holding the product's name, the number of items of that product in stock, 
# and the regular price of the product. There should be a method get_price that 
# receives the number of items to be bought and returns a the cost of buying that many 
# items, where the regular price is charged for orders of less than 10 items, a 10% 
# discount is applied for orders of between 10 and 99 items, and a 20% discount is 
# applied for orders of 100 or more items. There should also be a method 
# called make_purchase that receives the number of items to be bought and 
# decreases amount by that much.

name=input('Enter the name :')
amount=int(input('Enter the no. of products :'))
price=int(input('Enter the price :'))
class Product :
    def __init__(self,name,n,price) :
        self.name=name
        self.n=n
        self.price=price
    def make_purchase(self) :
        if 0<self.n<10 :
            return self.total
        elif 9<self.n<100 :
            return self.total-(self.total*0.1)
        elif self.n>=100 :
            return self.total-(self.total*0.2)
    def get_price(self) :
        self.total=self.price*self.n
        self.total=self.make_purchase()
        print('Total amount to be paid :',self.total)
c1=Product(name,amount,price)
c1.get_price()
