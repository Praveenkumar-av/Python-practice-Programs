# Write a class called Wordplay. It should have a field that holds a list of words. The 
# user of the class should pass the list of words they want to use to the class. There 
# should be the following methods:
# o words_with_length(length) — returns a list of all the words of length length
# o starts_with(s) — returns a list of all the words that start with s
# o ends_with(s) — returns a list of all the words that end with s
# o palindromes() — returns a list of all the palindromes in the list
# o only(L) — returns a list of the words that contain only those letters in L
# o avoids(L) — returns a list of the words that contain none of the letters in L

n=int(input('Enter the no. of words :'))
lst=[]
print('Enter the words :')
for i in range(n) :
    lst.append(input())
n=int(input('Enter the length of word :'))
s=input('Enter the string s :')
l=input('Enter the string for L')
class wordplay :
    def __init__(self,lst,n,s,l) :
        self.lst=lst
        self.lst1=[]
        self.lst2=[]
        self.lst3=[]
        self.lst4=[]
        self.lst5=[]
        self.lst6=[]
        self.n=n
        self.s=s
        self.l=l
    def words_with_length(self) :
        for w in self.lst :
            if self.n==len(w) :
                self.lst1.append(w)
        return self.lst1
    def starts_with(self) :
        for w in self.lst :
            if w.startswith(self.s) :
                self.lst2.append(w)
        return self.lst2
    def ends_with(self) :
        for w in self.lst :
            if w.endswith(self.s) :
                self.lst3.append(w)
        return self.lst3
    def palindromes(self) :
        for w in self.lst :
            if w==w[::-1] :
                self.lst4.append(w)
        return self.lst4
    def only(self) :
        for w in self.lst :
            for ch in w :
                if ch not in self.l :
                    break
            else :
                self.lst5.append(w)
        return self.lst5
    def avoids(self) :
        for w in self.lst :
            for ch in w :
                if ch in self.l :
                    break
            else :
                self.lst6.append(w)
        return self.lst6

case1=wordplay(lst,n,s,l)
print('Words with length',len,':',case1.words_with_length())
print('Words starts with',s,':',case1.starts_with())
print('Words ends with',s,':',case1.ends_with())
print('Palindrome words :',case1.palindromes())
print('Words that only contains',list(l),':',case1.only())
print('Words that does not contains',list(l),':',case1.avoids())