#  In calculus, the derivative of x^4 is 4x^3. The derivative of x5 is 5x4. The derivative of x^6 is
# 6x^5. This pattern continues. Write a program that asks the user for input
# like x^3 or x^25 and prints the derivative. For example, if the user enters x^3, the program
# should print out 3x^2.

exp=input('Enter the expression :')
index=exp.find('^')
if index==-1 :
    num=int(exp[0:len(exp)-1])
    print(num)
elif index==1 :
    power=int(exp[index+1:len(exp)])
    print('{}x^{}'.format(power,power-1))
elif index>1 :
    num=int(exp[0:index-1])
    power=int(exp[index+1:len(exp)])
    print('{}x^{}'.format(power*num,power-1))
