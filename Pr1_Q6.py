# Given a dictionary that contains the words in English language as key and Spanish words as value.
# Write a program to convert the given text in English to Spanish.
# Example:
# Input: Hello Good Morning!. Nice day. Education is the best
# Output: Hola Buenos dias!. Simpatico dia. Educacion es la major

d={'Hello':'Hola','Good':'Buenos','Morning!.':'dias!.','Nice':'Simpatico','day':'dia','Education':'Education','is':'es','the':'la','best':'major'}
lst=[x for x in input('Enter the string :').split(' ')]
for i in lst :
    print(d[i],end=' ')