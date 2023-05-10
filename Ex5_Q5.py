str=input('Enter a string :')
new_string=''
n=len(str)
for i in range(n) :
    if i==1 :
        new_string+='*'
    else :
        new_string+=str[i]
new_string+='!!!'
print(new_string)
