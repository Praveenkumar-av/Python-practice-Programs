# A simple way of encrypting a message is to rearrange its characters. One way to
# rearrange the characters is to pick out the characters at even indices, put them first
# in the encrypted string, and follow them by the odd characters. For example, the
# string message would be encrypted as msaeesg because the even characters
# are m, s, a, e (at indices 0, 2, 4, and 6) and the odd characters are e, s, g (at indices
# 1, 3, and 5).
# a. Write a program that asks the user for a string and uses this method to encrypt
# the string.
# b. Write a program that decrypts a string that was encrypted with this method.

str=input('Enter a string :')
# Encryption

n=len(str)
en_string=str[0:n:2]+str[1:n:2]  # encrypted string

# Decryption
half=n//2 if n%2==0 else (n//2)+1  # half of the string
str1=en_string[0:half]  # first half of encryped string
str2=en_string[half:n]  # second half of encrypted string
de_string=''
n1=len(str1)
for i in range(n1) :
    de_string+=str1[i]
    if not(i==n1-1 and n%2!=0) :
        de_string+=str2[i]

print('Encrypted string :',en_string)
print('Decrypted string :',de_string)