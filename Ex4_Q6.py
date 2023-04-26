# Write a function called binom that takes two integers n and k and returns the
# binomial coefficient n C k. The definition is n C k = n!/(k!(n-k)!).

def factorial(num) :
    f=1
    for i in range(1,num+1) :
        f*=i
    return f
def binom(n,k) :
    return factorial(n)/(factorial(k)*factorial(n-k))
n,k=[int(x) for x in input('Enter the Combination in the form of nCk :').split('C')]
result=binom(n,k)
print(result)
