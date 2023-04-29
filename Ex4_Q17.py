# a. Write a function called primes that is given a number n and returns a list of
# the first n primes. Let the default value of n be 100.
# b. Modify the function above so that there is an optional argument
# called start that allows the list to start at a value other than 2. The function
# should return the first n primes that are greater than or equal to start. The
# default value of start should be 2.

def primes(n=2) :
    lst=[]
    for i in range(n,101) :
        for j in range(2,i) :
            if i%j==0 :
                break
        else :
            lst.append(i)
    return lst
n=input("Enter start number : (if not enter 'n')")
if n.isnumeric() :
    n=int(n)
    if 2<n<=100 :
        lst=primes(n)
else :
    lst=primes()
print(lst)