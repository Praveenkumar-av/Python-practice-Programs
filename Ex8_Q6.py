class InsufficientFundsException(Exception) :
    def __init__(self,amount) :
        self.amount=amount
        
class LowBalancePenaltyException(Exception) :
    def __init__(self,amount) :
        self.amount=amount
        
class checkingAccount :
    def __init__(self,amount) :
        self.balance=1000
        self.amount=amount
    def deposit(self) :
        self.balance+=self.amount
        print('Amount deposited!')
    def withdraw(self) :
        try :
            if self.balance-self.amount<0 :
                raise InsufficientFundsException(self.amount)
            elif self.balance-self.amount<500 :
                raise LowBalancePenaltyException(self.amount)
            else :
                self.balance-=self.amount
                print('Amount withdrawed')
        except InsufficientFundsException :
            print('InsufficientFundsExeption')
        except LowBalancePenaltyException :
            print('LowBalancePenaltyExeption')
            
class data(checkingAccount) :
    def __init__(self,amount) :
        self.amount=amount
        super().__init__(self.amount)
    def pass_data(self) :
        q=input('Deposit(d) or Withdraw(w) :')
        if q=='d' :
            self.deposit()
        elif q=='w' :
            self.withdraw()

amount=int(input('Enter the amount :'))
person1=data(amount)
person1.pass_data()
