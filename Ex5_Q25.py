# In algebraic expressions, the symbol for multiplication is often left out, as in 3x+4y or
# 3(x+5). Computers prefer those expressions to include the multiplication symbol,
# like 3*x+4*y or 3*(x+5). Write a program that asks the user for an algebraic
# expression and then inserts multiplication symbols where appropriate.

exp=input('Enter the expression :')
result=exp[0:1]
for i in range(1,len(exp)) :
    if exp[i]=='(' :
        if exp[i-1].isalpha() or exp[i-1].isnumeric() or exp[i-1]==')':
            result+='*'
    elif exp[i].isalpha() :
        if exp[i-1].isalpha() or exp[i-1].isnumeric() or exp[i-1]==')':
            result+='*'
    result+=exp[i]
print(result)