# Write a program that generates the 26-line block of letters partially shown below. Use
# a loop containing one or two print statements.
# abcdefghijklmnopqrstuvwxyz
# bcdefghijklmnopqrstuvwxyza
# cdefghijklmnopqrstuvwxyzab
# ...
# yzabcdefghijklmnopqrstuvwx
# zabcdefghijklmnopqrstuvwxy

str='abcdefghijklmnopqrstuvwxyz'
for i in range(26) :
    print(str[i:26:1]+str[0:i:1])