# Write a function that accepts an encoded string as a parameter. This string will contain a first name,
# last name, and an id. Values in the string can be separated by any number of zeros. The id is a
# numeric value but will contain no zeros. The function should parse the string and return a Python
# dictionary that contains the first name, last name, and id values.
# Example:
# Input: "Robert000Smith000123".
# Output:
# { "first_name": "Robert", "last_name": "Smith", "id": "123" }

# import argparse
# parser=argparse.ArgumentParser()
# parser.addargument('str',type=str,help='Please enter a string!')
# args=parser.parse_args()
# s=args.str
# print(s)

str=input('Enter the string :')
i=0
n=len(str)
d={}
k=0
while i<n and k<3:
    ch=str[i]
    if ch=='0' or ch.isspace() :
        i+=1
        continue
    else :
        j=i
        s=''
        while j<n and str[j]!='0' and not(str[j].isspace()) :
            s+=str[j]
            j+=1
        if k==0 :
            d['first_name']=s
        elif k==1 :
            d['last_name']=s
        else :
            d['id']=s
        del s
        i=j
        k+=1
print(d)
