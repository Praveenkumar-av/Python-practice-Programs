# Our number system is called base 10 because we have ten digits: 0, 1, …, 9. Some
# cultures, including the Mayans and Celts, used a base 20 system. In one version of
# this system, the 20 digits are represented by the letters A through T. Here is a table
# showing a few conversions:
# 10 20 |10  20  |10 20  |10 20
# 0  A  |8   I   |16 Q   |39 BT
# 1  B  |9   J   |17 R   |40 CA
# 2  C  |10  K   |18 S   |41 CB
# 3  D  |11  L   |19 T   |60 DA
# 4  E  |12  M   |20 BA  |399 TT
# 5  F  |13  N   |21 BB  |400 BAA
# 6  G  |14  O   |22 BC  |401 BAB
# 7  H  |15  P   |23 BD  |402 BAC

def base_20(num) :
    d={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T'}
    s=''
    while(num) :
        s+=d[num%20]
        num//=20
    s=s[::-1]
    return s

n=int(input('Enter the number :'))
print(base_20(n))