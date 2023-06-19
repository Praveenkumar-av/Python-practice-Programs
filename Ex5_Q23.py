# A more general version of the above technique is the rail fence cipher, where instead
# of breaking things into evens and odds, they are broken up by threes, fours or
# something larger. For instance, in the case of threes, the string secret message would
# be broken into three groups. The first group is sr sg, the characters at indices 0, 3, 6,
# 9 and 12. The second group is eemse, the characters at indices 1, 4, 7, 10, and 13.
# The last group is ctea, the characters at indices 2, 5, 8, and 11. The encrypted message
# is sr sgeemsectea.
# a. Write a program the asks the user for a string and uses the rail fence cipher in
# the threes case to encrypt the string.
# b. Write a decryption program for the threes case.
# c. Write a program that asks the user for a string, and an integer determining
# whether to break things up by threes, fours, or whatever. Encrypt the string
# using the rail-fence cipher.
# d. Write a decryption program for the general case.

s=input('Enter the string :')
b=int(input('Enter the no. of breaks :'))
n=len(s)
lst=[]

# Encryption
for i in range(b) :
    lst.append(s[i:n:b])
en_string=''.join(lst)
print('Encrypted string:',en_string)

# Decryption
index_list=[]
for i in range(b) :
    index_list+=list(range(i,n,b))

de_string=''
for i in range(n) :
    for j in range(n) :
        if i==index_list[j] :
            index=j
            break
    de_string+=en_string[index]
print('Decrypted string :',de_string)