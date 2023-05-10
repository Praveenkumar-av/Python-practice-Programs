str=input('Enter the string :')
strnew=''
for ch in str :
    if not(ch=='.' or ch==',') :
        strnew+=ch.upper()
print(strnew)
