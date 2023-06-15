#  An anagram of a word is a word that is created by rearranging the letters of the
# original. For instance, two anagrams of idle are deli and lied. Finding anagrams that
# are real words is beyond our reach until the chapter on text files. Instead, write a
# program that asks the user for a string and returns a random anagram of the string—
# in other words, a random rearrangement of the letters of that string.

word=input('Enter the word :')
n=len(word)
random_word=''
index=list(range(n))  # list of all index
from random import randint
while(n!=len(random_word)) :
    i=randint(0,n-1)  # random index generator
    if i in index :
        random_word+=word[i]
        index.remove(i)  # removing the index
print(random_word)