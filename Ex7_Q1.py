# Create a class, "PrimeTester", that defines one method "Boolean isPrime(int n)".When this function is
# called the implementing class should determine if the given "n" is prime or not. Create a class
# "SimpleTester" that inherits "PrimeTester" and uses a naive method to determine if a given number is
# a prime or not.

num=int(input('Enter a number :'))
class primeTester :
    def __init__(self,num) :
        self.num=num
    
    def isprime(self) :
        if self.num==1 or self.num==0:
            return False
        for i in range(2,self.num) :
            if self.num%i==0 :
                return False
        else :
            return True

class simpleTester(primeTester) :
    def testprime(self) :
        return super().isprime()

t1=simpleTester(num)
bool=t1.testprime()
if bool :
    print('Prime number ')
else :
    print('Not a prime number ')
    