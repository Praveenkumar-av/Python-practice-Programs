# Write a program that asks the user for a large integer and inserts commas into it
# according to the standard American convention for commas in large numbers. For
# instance, if the user enters 1000000, the output should be 1,000,000.

num=input('Enter the number :')
num=num[::-1]    # reversing the number
str=num[0]
for i in range(1,len(num)) :
    if i%3==0 :
        str+=','    # adding comma for each 3 degit   
    str+=num[i]
str=str[::-1]      # reversing back the original form
print(str)