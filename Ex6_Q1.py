# Write a class called Investment with fields called principal and interest. The 
# constructor should set the values of those fields. There should be a method 
# called value_after that returns the value of the investment after n years. The formula 
# for this is p(1+i)^n
# , where p is the principal, and i is the interest rate. It should also use 
# the special method __str__ so that printing the object will result in something like 
# below:
# Principal - $1000.00, Interest rate - 5.12%

p=int(input('Enter the principal amount :'))
i=int(input('Enter the Intereest :'))
n=int(input('Enter the no. of years :'))
class Investment :
    def __init__(self,p,i,n) :
        self.pr=p
        self.i=i
        self.no=n
        self.amount=0
    def value_after(self) :
        self.amount=self.pr*((1+self.i)**self.no)
    def __str__(self) :
        print('Principal :',self.pr)
        print('Interest :',self.i)
        print('Amount :',self.amount)
s1=Investment(p,i,n)
s1.value_after()
s1.__str__()
