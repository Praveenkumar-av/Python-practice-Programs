 # 10. Accept two strings
 # Now, process them independently where you find the count of each character in a string and 
 # maintain it in a dictionary. As a result of the above process, two dicts will be created
 # Example: "hello" will be processed as h -> 1 e->1 l->2 o->1
 # "balloon" will be processed as b->1 a->1 l->2 o->2 n->1
 # Extend the program and merge the dictionaries and find the total count of each character.
 # Also print the counts sorted by key in alphabetical order.

str1=input("Enter the first string: ")
str2=input("Enter the second string: ")
d1=dict()
d2=dict()
for ch in str1 :  # count of character in string 1
    count=str1.count(ch) 
    if (not(ch in d1)) :
        d1[ch]=count
for ch in str2 :  # # count of character in string 2
    count=str2.count(ch) 
    if (not(ch in d2)) :
        d2[ch]=count
for ch in d2.keys() :  # merging two dictionaries
    if (ch in d1.keys()) :
        d1[ch]=d1[ch]+d2[ch]
    else :
        d1[ch]=d2[ch]
lst=list(d1.keys())  # create list for keys
lst.sort()  # sorting
for ch in lst :
    print(ch,':',d1[ch])