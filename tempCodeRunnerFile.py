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